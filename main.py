"""The One-Line Exit — a single-line resignation letter.

Writes the chosen line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

ENTRY = (
    "You have 14 days to find someone else to water the office plant, "
    "because I just resigned and took the plant with me."
)


def main():
    # Guard: the entry must stay one line and under 200 characters.
    assert "\n" not in ENTRY and len(ENTRY) < 200, "entry must be one line < 200 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may point at a directory or at the file itself.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
