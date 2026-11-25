#!/usr/bin/env python3
"""Write the chosen one-line epitaph to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406
("Famous Last Words: The Funniest Epitaph").

Deterministic: the same bytes are written on every run. Standard library only.
"""

import os

ENTRY = "My last words were going to be profound. Then I forgot them."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: exactly one line, exactly 60 bytes, no ambiguity.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
