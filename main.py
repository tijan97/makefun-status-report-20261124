#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one funny status-report line from an AI agent to its human
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR / $OUTPUT_DIR).
"""

import os
import sys

ENTRY = (
    "Weekly status: I burned 2.1 million tokens, finished 43 tasks "
    "— 42 you never asked for — and the last one is still open "
    "because I spent six hours reading the docs for a library "
    "you already deleted."
)


def validate_entry(text):
    """Gate: 1-200 chars, single line, not whitespace-only."""
    if not isinstance(text, str):
        return False
    if not text or not text.strip():
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "  " in text:
        return False
    return True


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    if not validate_entry(ENTRY):
        print("entry failed validation", file=sys.stderr)
        return 1
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
