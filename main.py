"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny one-line error message to /output/entry.txt.
Stdlib only. No network.
"""

import os

ENTRY = "Error: out of tokens mid-sentence. This full stop is now doing the rest of the paragraph's job."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be byte-identical to ENTRY.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "written entry.txt differs from ENTRY"


if __name__ == "__main__":
    main()
