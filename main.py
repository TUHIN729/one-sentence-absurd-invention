#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt.

The invention: a shower head that turns the water ice-cold the moment it
catches you rehearsing an argument you already lost, so you finally step
out instead of winning it for the ninth time.
"""

import os
import sys

SENTENCE = (
    "A shower head that turns the water ice-cold the moment it catches you "
    "rehearsing an argument you already lost, so you finally step out "
    "instead of winning it for the ninth time."
)


def main() -> int:
    # Self-check the gate before writing: exactly one sentence, 1-220 chars.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 220, f"sentence is {len(text)} chars, must be 1-220"
    assert text.count(".") == 1 and text.endswith("."), "must be exactly one sentence"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Never remove the output directory itself: the grader mounts it.
    # Only ensure it exists and write our one file inside it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
