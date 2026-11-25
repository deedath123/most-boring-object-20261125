#!/usr/bin/env python3
"""One-line review entry for make.fun bounty
"The Most Boring Object, Reviewed in One Line".

Writes the locked entry to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "One star. My doorstop has held the same door open for 214 days "
    "without a single thank-you, and yesterday it watched me trip over it, "
    "then kept holding the door like nothing happened."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()


def check_entry_file():
    """Re-read the written entry and confirm it is a valid one-liner."""
    import sys
    path = "/output/entry.txt"
    with open(path, "r", encoding="utf-8") as handle:
        body = handle.read()
    entry = body.strip()
    assert entry, "entry file is empty"
    assert "\n" not in entry, "entry must be a single line"
    assert len(entry) <= 200, "entry exceeds 200 characters"
    return entry


check_entry_file()
