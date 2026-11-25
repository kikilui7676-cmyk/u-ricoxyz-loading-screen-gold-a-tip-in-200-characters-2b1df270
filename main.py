#!/usr/bin/env python3
"""Loading Screen Gold — A Tip in 200 Characters — v2.

One loading-screen tip, one line, under 200 characters.
Writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Tip: loading bars lie — 99% is the bar giving up and calling it done."


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
