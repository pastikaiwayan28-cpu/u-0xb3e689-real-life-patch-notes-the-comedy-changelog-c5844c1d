#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — entry program.

Writes a single original one-line comedy patch note to /output/entry.txt.

Deterministic by design: no input, no randomness, no network, no clock.
Every run writes the exact same bytes.
"""

import os
from pathlib import Path

ENTRY = (
    "v3.2.1: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 at 3 a.m. for no reason."
)

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
