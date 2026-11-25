"""One Line, One Laugh — entry program (v2, revised).

Writes a single original funny line to /output/entry.txt.
Python 3, stdlib only, fully deterministic, no network.
"""

import os
from pathlib import Path

LINE = (
    "My password manager forgot my password. Now we're both locked out "
    "of my life, and neither of us is talking about it."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    # Gate: 1-200 chars, UTF-8, not whitespace-only, single line.
    assert "\n" not in text and "\r" not in text, "line must be single-line"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be whitespace-only"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
