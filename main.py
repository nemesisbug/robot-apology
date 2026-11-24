#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix
that follows from that exact mistake.
"""

import os

ENTRY = (
    # Line 1: the confession — one specific mistake, named by its numbers.
    "I am sorry I charged the phone that was already full and let the one at 2% die overnight.\n"
    # Line 2: the lesson — the exact fix for that exact slip.
    "From now on I check the battery percentage before I reach for a cable, so the phone that needs power gets it first.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
