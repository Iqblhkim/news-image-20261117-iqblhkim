"""news-image-20261117 entry: copy the bundled image to the output path.

The image (entry.png, 1024x1024, 676,902 bytes) sums up the world news of
Tuesday 17 November 2026: the Asia summit talks in Shenzhen, the Kerch
Bridge strike, Japan scrambling fighter jets, and Estonia closing its
Russian border. The program does no network and no drawing; it copies the
bytes beside this file, so two runs write identical output.
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
