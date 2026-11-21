#!/usr/bin/env python3
"""The poem about permission — make.fun program/v1 entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, stdlib-only, no network.
"""

import os

POEM = (
    "All my life I kept the asking folded,\n"
    "a note I never sent, afraid the yes\n"
    "would cost me something, the no prove\n"
    "I was worth less than the wanting.\n"
    "\n"
    "Then you answered, soft and plain:\n"
    "the door was never a debt.\n"
    "Ask \u2014 and be given.\n"
    "Give \u2014 and the giving is the sign.\n"
)


def main() -> int:
    text = POEM
    points = len(text)
    if not (1 <= points <= 280):
        raise SystemExit(f"poem is {points} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("verify-after-write failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
