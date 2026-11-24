# SPDX-License-Identifier: MIT
"""One-Star Review of Something Essential entry (Python 3, stdlib only).

Writes one fixed deadpan one-star review of sleep to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: every run writes exactly the same bytes.
"""

import os
from pathlib import Path

ENTRY = (
    "One star. Sleep takes a third of my life, refuses to arrive when "
    "summoned, and leaves the moment the alarm finally makes it worth staying."
)


def entry_text() -> str:
    return ENTRY


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
