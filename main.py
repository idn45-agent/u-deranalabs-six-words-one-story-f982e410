#!/usr/bin/env python3
"""Six Words, One Story — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is one complete six-word story.
"""

import os

ENTRY = "Sold everything, kept the dog's leash."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
