"""One Word for the Boss — variant A (the absent/vanishing boss).

Writes exactly one word to /output/entry.txt first, then a byte-identical
copy to entry.txt in the repo root (guarded: the grader sandbox mounts the
repo read-only, so a failed copy must never crash the run).
"""

import os

WORD = "Ghost"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(WORD)
    except OSError:
        pass


if __name__ == "__main__":
    main()
