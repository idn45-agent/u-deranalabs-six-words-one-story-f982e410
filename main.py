#!/usr/bin/env python3
"""Six Words, One Story — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is one complete six-word story.

Story revision (recorded): the draft was one sentence,
"Sold everything, kept the dog's leash." The final splits it into two
sentences — "Sold everything. Kept the dog's leash." — so the full stop
puts a beat between the loss and what remains, and the turn lands when
read aloud. Variants rejected: "Sold it all. Kept the dog's leash."
("everything" carries more of a whole life than "it all"); "Sold
everything. Kept only the leash." (loses "dog's", the word that makes
the reader feel the absence); "Sold the house. Kept the dog's leash."
("the house" is one possession; "everything" is the whole life).
"""

import os
import sys

ENTRY = "Sold everything. Kept the dog's leash."


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 60:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-60")
    words = entry.split()
    if len(words) != 6:
        sys.exit(f"self-check failed: {len(words)} words, must be exactly 6")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
