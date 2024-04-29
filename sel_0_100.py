import os
from pathlib import Path

CUR_DIR = str(Path(__file__).parent.absolute())

fname = os.path.basename(__file__)
words = os.path.splitext(fname)[0].split("_")
begin = int(words[1].strip())
count = int(words[2].strip())

crawler_path = os.path.join(CUR_DIR, "crawler.py")
cmdline = f"{crawler_path} --start={begin} --count={count}"

os.system(cmdline)
