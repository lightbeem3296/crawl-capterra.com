import inspect
import os
from datetime import datetime
from typing import Tuple

import colorama

colorama.init()

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATETIME_FORMAT = "%H:%M:%S"


def log_inf(text: str):
    __log(
        time=datetime.now().strftime(DATETIME_FORMAT),
        mark=f"{colorama.Fore.LIGHTGREEN_EX}[+]",
        text=text,
    )


def log_warn(text: str):
    filename, linenumber, funcname = __get_info()
    __log(
        time=datetime.now().strftime(DATETIME_FORMAT),
        mark=f"{colorama.Fore.YELLOW}[!]",
        text=text,
        desc=f"({filename}:{linenumber} {funcname})",
    )


def log_err(text: str):
    filename, linenumber, funcname = __get_info()
    __log(
        time=datetime.now().strftime(DATETIME_FORMAT),
        mark=f"{colorama.Fore.LIGHTRED_EX}[-]",
        text=text,
        desc=f"({filename}:{linenumber} {funcname})",
    )


def __log(time: str, mark: str, text: str, desc: str = ""):
    if not "\n" in text:
        print(
            f"{colorama.Fore.CYAN}{time}"
            + f" {mark}"
            + f" {colorama.Fore.RESET}{text}"
            + f" {colorama.Fore.LIGHTBLACK_EX}{desc}"
            + f"{colorama.Fore.RESET}"
        )
    else:
        lines = text.replace("\r", "").split("\n")

        print(
            f"{colorama.Fore.CYAN}{time}"
            + f" {mark}"
            + f" {colorama.Fore.RESET}{lines[0].strip()}"
            + f" {colorama.Fore.LIGHTBLACK_EX}{desc}"
            + f"{colorama.Fore.RESET}"
        )
        for line in lines[1:]:
            print(" " * (len(time) + 5) + line)


def __get_info() -> Tuple[str, int, str]:
    """
    Returns file name, line number and function name.
    """
    funcname, filename, linenumber = "#", "#", 0
    cur_frame = inspect.currentframe()
    if cur_frame != None and cur_frame.f_back != None and cur_frame.f_back.f_back != None:
        frame_info = inspect.getframeinfo(cur_frame.f_back.f_back)
        filename = os.path.basename(frame_info.filename)
        linenumber = frame_info.lineno
        funcname = frame_info.function
    return filename, linenumber, funcname


if __name__ == "__main__":

    def main():
        log_inf("info log")
        log_inf("info\nlog")
        log_warn("warning log")
        log_warn("warning\nlog")
        log_err("error log")
        log_err("error\nlog")

    main()
