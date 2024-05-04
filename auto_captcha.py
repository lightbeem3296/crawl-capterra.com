# pip install opencv_python

import datetime
import os
import time
import traceback
from pathlib import Path

import pyautogui

from liblogger import log_err, log_inf

CUR_DIR = str(Path(__file__).parent.absolute())
CAPTCHA_START_IMG_PATH = os.path.join(CUR_DIR, "captcha_start.png")
CAPTCHA_END_IMG_PATH = os.path.join(CUR_DIR, "captcha_end.png")


def main():
    try:
        log_inf("*** move this window for the captcha to be visible")
        log_inf("delay for 5 seconds ...")
        time.sleep(5)

        while True:
            # wait until captcha start
            log_inf("waiting for captcha detected ...")
            img_box = None
            while img_box == None:
                try:
                    img_box = pyautogui.locateOnScreen(CAPTCHA_START_IMG_PATH, confidence=0.7)
                except:
                    pass
                time.sleep(0.1)
            log_inf(f"captcha detected at {img_box}")

            logo_x, logo_y, _, _ = img_box
            pyautogui.moveTo(logo_x, logo_y, duration=0.1)
            pyautogui.mouseDown()

            # wait until captcha end
            log_inf("waiting for captcha done ...")
            start = datetime.datetime.now().timestamp()
            img_box = None
            while img_box == None:
                try:
                    if datetime.datetime.now().timestamp() - start > 20:
                        log_err("waiting timeout")
                        break
                    img_box = pyautogui.locateOnScreen(CAPTCHA_END_IMG_PATH, confidence=0.7)
                except:
                    pass
                time.sleep(0.1)
            pyautogui.mouseUp()
            log_inf(f"captcha done")

            time.sleep(0.1)
    except:
        traceback.print_exc()


if __name__ == "__main__":
    main()
    input("Press ENTER to exit.")
