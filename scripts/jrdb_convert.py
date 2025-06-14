#!/usr/bin/env python3
"""Convert JRDB fixed-width text files to CSV.

This script reads all files under ``~/jrdb_input`` assumed to be
SHIFT_JIS encoded fixed-width text files and outputs CSV versions
under ``~/jrdb_csv`` encoded in UTF-8.
"""

from __future__ import annotations

import os
from pathlib import Path
import pandas as pd


def convert_file(path: Path, out_dir: Path) -> None:
    """Convert a single fixed-width file to CSV."""
    df = pd.read_fwf(path, encoding="cp932", dtype=str, header=None)
    out_path = out_dir / (path.stem + ".csv")
    df.to_csv(out_path, index=False, encoding="utf-8")


def main() -> None:
    input_dir = Path(os.path.expanduser("~/jrdb_input"))
    output_dir = Path(os.path.expanduser("~/jrdb_csv"))
    output_dir.mkdir(parents=True, exist_ok=True)

    for f in input_dir.glob("*"):
        if f.is_file():
            convert_file(f, output_dir)


if __name__ == "__main__":
    main()
