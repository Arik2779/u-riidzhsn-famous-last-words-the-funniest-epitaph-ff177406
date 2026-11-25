#!/usr/bin/env python3
"""Write the chosen one-line epitaph to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406
("Famous Last Words: The Funniest Epitaph").

Deterministic: the same bytes are written on every run. Standard library only.
Self-check: the line is validated against the competition gate (1-150
characters, exactly one line, not only whitespace) before it is written.
"""

import os

ENTRY = "My last words were going to be profound. Then I forgot them."


def check_entry(line: str) -> None:
    """Validate the line against the competition gate before writing."""
    if not 1 <= len(line) <= 150:
        raise ValueError(f"entry must be 1-150 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    check_entry(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: exactly one line, exactly 60 bytes, no ambiguity.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
