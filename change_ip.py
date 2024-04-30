import base64
import os
import random
import subprocess
import time
import traceback
from pathlib import Path

import requests

from liblogger import log_err, log_inf

CHANGE_INTERVAL = 300.0
SERVER_LIST_URL = "http://www.vpngate.net/api/iphone/"
SERVER_IP_HISTORY = []
SERVER_LIST = []
CUR_DIR = str(Path(__file__).parent.absolute())
OVPN_FILE_NAME = "server.ovpn"
OVPN_FILE_PATH = os.path.join(CUR_DIR, OVPN_FILE_NAME)
OPENVPN_PATH = r"C:\Program Files\OpenVPN\bin\openvpn.exe"


def fetch_servers():
    try:
        global SERVER_LIST
        resp = requests.get(SERVER_LIST_URL)
        if resp.status_code == 200:
            SERVER_LIST = []
            server_list_str = resp.text
            for server_string in server_list_str.replace("\r", "").split("\n")[2:-2]:
                (
                    HostName,
                    IP,
                    Score,
                    Ping,
                    Speed,
                    CountryLong,
                    CountryShort,
                    NumVpnSessions,
                    Uptime,
                    TotalUsers,
                    TotalTraffic,
                    LogType,
                    Operator,
                    Message,
                    OpenVPN_ConfigData_Base64,
                ) = server_string.split(",")
                server = {
                    "HostName": HostName,
                    "IP": IP,
                    "Score": Score,
                    "Ping": Ping,
                    "Speed": Speed,
                    "CountryLong": CountryLong,
                    "CountryShort": CountryShort,
                    "NumVpnSessions": NumVpnSessions,
                    "Uptime": Uptime,
                    "TotalUsers": TotalUsers,
                    "TotalTraffic": TotalTraffic,
                    "LogType": LogType,
                    "Operator": Operator,
                    "Message": Message,
                    "OpenVPN_ConfigData_Base64": OpenVPN_ConfigData_Base64,
                }
                SERVER_LIST.append(server)
            SERVER_LIST = SERVER_LIST[: len(SERVER_LIST) >> 1]
            SERVER_LIST = random.sample(SERVER_LIST, len(SERVER_LIST))
        else:
            log_err(f"resp error: {resp.status_code}")
    except:
        traceback.print_exc()


def main():
    try:
        openvpn_process = None
        while True:
            try:
                # select server
                server_to_connect = None
                for server in SERVER_LIST:
                    if server["IP"] in SERVER_IP_HISTORY:
                        break
                    else:
                        server_to_connect = server

                if server_to_connect == None:
                    log_err("server not found in list.")
                    log_inf("update server list ...")
                    fetch_servers()
                    for server in SERVER_LIST:
                        server_to_connect = server
                        break

                if server_to_connect == None:
                    log_err("server not found")
                    continue

                # save to config file
                with open(OVPN_FILE_PATH, "wb") as f:
                    f.write(base64.b64decode(server_to_connect["OpenVPN_ConfigData_Base64"]))

                # connect to server
                if openvpn_process != None:
                    openvpn_process.kill()
                openvpn_process = subprocess.Popen([OPENVPN_PATH, "--config", OVPN_FILE_PATH])

                # delay
                log_inf(f"delay for {CHANGE_INTERVAL} secs ...")
                time.sleep(CHANGE_INTERVAL)
            except:
                traceback.print_exc()
    except:
        traceback.print_exc()


def test():
    subprocess.run([OPENVPN_PATH, "--config", OVPN_FILE_PATH])


if __name__ == "__main__":
    main()
    # test()
    input("Press ENTER to exit.")
