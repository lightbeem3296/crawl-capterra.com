import base64
import json
import os
import shutil
import socket
import subprocess
import time
import traceback
from datetime import datetime
from pathlib import Path
from random import randint
from typing import Any, Optional

import userpaths

from liblogger import log_err, log_inf
from libwebsocket import WebSocketServer

CUR_DIR = str(Path(__file__).parent.absolute())
TEMP_DIR = os.path.join(CUR_DIR, "temp")
EXTENSION_DIR = os.path.join(CUR_DIR, "ext")


class ChromeElem:
    def __init__(self, selector: Optional[str] = None):
        self.selector = selector


class Chrome:
    def __init__(
        self,
        init_url: str = "http://example.com",
        width: int = 0,
        height: int = 0,
        block_image: bool = False,
        user_data_dir: Optional[str] = None,
    ):
        self.__init_url = init_url
        self.__width = width
        self.__height = height
        self.__block_image = block_image
        self.__user_data_dir = user_data_dir
        self.__process = None
        self.__client_unit = None

    def __find_port(self) -> int:
        with socket.socket() as s:
            s.bind(("", 0))  # Bind to a free port provided by the host
            return s.getsockname()[1]  # Return the assigned port number

    def __send_command(self, msg: str, payload: Optional[str] = None) -> Any:
        ret = None
        try:
            if self.__client_unit != None:
                if payload != None:
                    self.__client_unit.send(
                        json.dumps(
                            {
                                "msg": msg,
                                "payload": payload,
                            }
                        )
                    )
                else:
                    self.__client_unit.send(
                        json.dumps(
                            {
                                "msg": msg,
                            }
                        )
                    )
                resp = self.__client_unit.recv()
                if resp != None:
                    js_res = json.loads(resp)["result"]
                    if js_res != "<undefined>":
                        ret = js_res
                else:
                    log_err("resp is none")
                    time.sleep(0.5)
            else:
                log_err("client_unit is none")
        except:
            traceback.print_exc()
        return ret

    def start(self):
        chrome_path = ""
        chrome_est_paths = [
            userpaths.get_local_appdata() + "\\Google\\Chrome\\Application\\Chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe",
            "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe",
        ]
        for chrome_est_path in chrome_est_paths:
            if os.path.isfile(chrome_est_path):
                chrome_path = chrome_est_path
                break

        if os.path.isfile(chrome_path):
            # find free port
            port = self.__find_port()

            # start socket server
            websocket_server = WebSocketServer("127.0.0.1", port)
            websocket_server.start()

            # copy extension to temp folder
            ext_dir = os.path.join(TEMP_DIR, f"ext_{datetime.now().timestamp()}")
            shutil.copytree(EXTENSION_DIR, ext_dir, dirs_exist_ok=True)

            # set extension port number
            background_js_path = os.path.join(ext_dir, "background.js")
            with open(background_js_path, "r") as f:
                background_js_content = f.read()
            with open(background_js_path, "w") as f:
                f.write(background_js_content.replace("{PORT}", f"{port}"))

            # remove old profile folder
            if self.__user_data_dir == None:
                self.__user_data_dir = os.path.join(TEMP_DIR, "profile")

            # start chrome
            cmd = [chrome_path]
            cmd.append(f"--user-data-dir={self.__user_data_dir}")
            if os.path.isdir(ext_dir):
                cmd.append(f"--load-extension={ext_dir}")

            if self.__width * self.__height != 0:
                cmd.append(f"--window-size={self.__width},{self.__height}")

            if self.__block_image:
                cmd.append("--blink-settings=imagesEnabled=false")

            if self.__init_url != "":
                cmd.append(self.__init_url)

            user_agent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{randint(90, 120)}.{randint(0, 100)}.{randint(0, 100)}.{randint(0, 100)} Safari/537.{randint(0, 100)} Edg/{randint(90, 120)}.0.{randint(1000, 2000)}.{randint(0, 100)}"
            cmd.append(f"--user-agent={user_agent}")

            self.__process = subprocess.Popen(cmd)

            # accept
            self.__client_unit = websocket_server.accept()
            log_inf("client connected")
        else:
            log_err("chrome.exe not found")

    def quit(self):
        if self.__process != None:
            self.__process.terminate()
            self.__process = None

        if self.__client_unit != None:
            self.__client_unit.close()
            self.__client_unit = None

        self.__width = 0
        self.__height = 0
        self.__block_image = True

    def run_script(self, script: str) -> Optional[str]:
        return self.__send_command("runScript", script)

    def url(self) -> Optional[str]:
        return self.run_script("location.href")

    def goto(self, url2go: str, wait_timeout: float = 30.0, wait_elem_selector: Optional[str] = None) -> bool:
        ret = False
        try:
            timeout = False

            old_url = self.url()
            if old_url == url2go:
                self.run_script("location.reload()")
            else:
                self.run_script(f"location.href='{url2go}'")
                # wait for url changed
                start_tstamp = datetime.now().timestamp()
                while True:
                    if old_url != self.url():
                        break
                    if datetime.now().timestamp() - start_tstamp > wait_timeout:
                        log_err("timeout")
                        timeout = True
                        break

            # wait for element valid
            if not timeout:
                if wait_elem_selector != None:
                    start_tstamp = datetime.now().timestamp()
                    while True:
                        wait_elem = self.select_one(wait_elem_selector)
                        if wait_elem != None:
                            break
                        if datetime.now().timestamp() - start_tstamp > wait_timeout:
                            log_err("timeout")
                            timeout = True
                            break
            if not timeout:
                ret = True
        except:
            traceback.print_exc()
        return ret

    def cookie(self, domain: str) -> Any:
        return self.__send_command("getCookie", domain)

    def clear_cookie(self):
        return self.__send_command(
            "clearCookie",
        )

    def head(self) -> Optional[str]:
        self.run_script("document.head")

    def body(self) -> Optional[str]:
        self.run_script("document.body")

    def select(self, selector: str) -> list[ChromeElem]:
        ret = []
        jres = self.run_script(
            """
function getSelector(elm) {
    if (elm.tagName === 'BODY') return 'BODY';
    const names = [];
    while (elm.parentElement && elm.tagName !== 'BODY') {
        if (elm.id) {
            names.unshift('#' + elm.getAttribute('id'));
            break;
        } else {
            let c = 1, e = elm;
            for (; e.previousElementSibling; e = e.previousElementSibling, c++);
            names.unshift(elm.tagName + ':nth-child(' + c + ')');
        }
        elm = elm.parentElement;
    }
    return names.join('>');
}

var selectors = [];

var elemList = document.querySelectorAll('"""
            + selector
            + """');
for (var elem in elemList) {
    if (elem == elem * 1) {
        var selector = getSelector(elemList[elem]);
        selectors.push(selector);
    }
}

selectors;"""
        )
        if jres != None:
            for jitem in jres:
                ret.append(ChromeElem(jitem))
        return ret

    def select_one(self, selector: str) -> Optional[ChromeElem]:
        elems = self.select(selector=selector)
        if len(elems) > 0:
            return elems[0]
        else:
            return None

    def set_value(self, selector: str, value: str):
        b64value = base64.b64encode(value.encode()).decode()
        self.run_script(f"document.querySelector('{selector}').value=atob('{b64value}')")

    def click(self, selector: str):
        self.run_script(f"document.querySelector('{selector}').click()")


if __name__ == "__main__":
    chrome = Chrome(user_data_dir=os.path.join(TEMP_DIR, "profile"))
    chrome.start()

    chrome.goto(url2go="https://google.com", wait_elem_selector="#APjFqb")
    log_inf(str(chrome.url()))

    chrome.set_value(selector="#APjFqb", value="chrome")
    chrome.click(selector="[name=btnK]")

    log_inf("before clear cookie")
    log_inf(chrome.cookie("google.com"))
    chrome.clear_cookie()
    log_inf("after clear cookie")
    log_inf(chrome.cookie("google.com"))

    input("Press ENTER to exit.")
    chrome.quit()
