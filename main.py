#!/usr/bin/env python3
"""Entry for u-rama-melon-make-the-ai-judge-laugh-302d0825.

Writes one office-life joke, readable aloud in a single breath, to
/output/entry.txt (UTF-8, no trailing newline).
"""

import os

LINE = "My boss said 'work smarter, not harder,' then booked a 7 a.m. meeting to find out why we're behind."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
