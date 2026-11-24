#!/usr/bin/env python3
"""Make the Judge Smile — entry generator.

Writes the entry line (plus exactly one trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Self-checked gate, enforced before anything is written:
  * 1 <= len(LINE) <= 200 characters (the brief's one-line limit)
  * LINE == LINE.strip() — no leading or trailing whitespace
"""

import os

LINE = "This morning I finally learned why my dying plant is alive: the night guard waters it every shift, has never told me, and it has started leaning toward his chair."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry line out of range: {len(LINE)} chars"
    assert LINE == LINE.strip(), "entry line has leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
