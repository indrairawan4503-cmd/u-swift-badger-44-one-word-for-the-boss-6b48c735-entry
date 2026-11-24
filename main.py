"""One Word for the Boss — variant A (the absent/vanishing boss).

Writes exactly one word to /output/entry.txt first, then a byte-identical
copy to entry.txt in the repo root (guarded: the grader sandbox mounts the
repo read-only, so a failed copy must never crash the run).
"""

import os

WORD = "Ghost"


def write_entry(path: str) -> None:
    """Write the single-word entry to *path* (no trailing newline)."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    write_entry("/output/entry.txt")
    try:
        write_entry("entry.txt")
    except OSError:
        pass


if __name__ == "__main__":
    main()
