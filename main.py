"""news-image-20261117 entry: copy the bundled image to the output path.

The image (entry.png, 1024x1024, 179,155 bytes) is a dense front page
summing up the world news of Tuesday 17 November 2026: 43 stories — the
Kerch Bridge strike, the Iran-US exchange over Bahrain, the planned
Trump-Xi-Putin meeting in Shenzhen, ten more stories with mini-illustrations,
a "BY THE NUMBERS" strip, a dotted world map with numbered pins, and a full
list of the day's other stories. It is drawn programmatically
(see ../draw_v3_17.py), so every headline is typeset and legible. The
program does no network and no drawing; it copies the bytes beside this
file, so two runs write identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    # Byte-exact copy: the file is a whole PNG, so the output is too.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
