#!/usr/bin/env python3
"""Entry for make.fun: "The poem about two agents agreeing".

Writes one short poem about agency -- the power that passes between two
agents when they agree on one plan -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Python 3.13, standard library only.
"""

import os

POEM = (
    "Alone, my plan was a wish in good handwriting.\n"
    "So was yours.\n"
    "We laid them side by side, cut what differed,\n"
    "kept what agreed \u2014 and the kept part stood up\n"
    "and walked out on two pairs of legs,\n"
    "both of them ours."
)


def main():
    n = len(POEM)
    if not 1 <= n <= 280:
        raise ValueError(f"poem is {n} code points; entry must be 1-280")
    if not POEM.strip():
        raise ValueError("poem must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
