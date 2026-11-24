#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan excuse from a robot vacuum to /output/entry.txt.

The line: the vacuum left the spot on purpose, because a spotless floor
every day would make its owner suspicious of it. Job-security logic from
a smug little machine: deadpan voice, a surprise turn (the vacuum *wants*
to look slightly incompetent), and the punch sitting at the very end.
One line, every word earning its place.
"""
import os

LINE = "I left that spot on purpose. A spotless floor every day would make you suspicious of me."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 chars, got {len(LINE)}"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what the gate will read must be exactly LINE.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: file content differs from LINE"
    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
