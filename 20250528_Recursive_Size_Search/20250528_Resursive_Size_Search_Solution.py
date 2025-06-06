#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple

DEF_THRESHOLD_MB = 100

def human_readable(bytes_: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if bytes_ < 1000:
            return f"{bytes_:.1f} {unit}"
        bytes_ /= 1000
    return f"{bytes_:.1f} PB"

def dir_size(path: Path) -> int:
    # ↪ returns size in bytes
    total = 0
    for root, _, files in os.walk(path, followlinks=False):
        for f in files:
            try:
                total += (Path(root) / f).stat().st_size
            except OSError:
                continue
    return total

def load_paths(file: Path) -> List[str]:
    # read & clean list
    return [line.strip() for line in file.read_text().splitlines()
            if line.strip() and not line.lstrip().startswith("#")]

def main() -> None:
    env_thr = int(os.getenv("SIZE_THRESHOLD_MB", DEF_THRESHOLD_MB))
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int,
                        help=f"Size alert threshold in MB (default {env_thr})")
    parser.add_argument("listfile", nargs="?", default="directories.txt",
                        help="File containing directory paths")
    args = parser.parse_args()
    threshold_mb = args.threshold if args.threshold is not None else env_thr

    paths = load_paths(Path(args.listfile))

    # TODO: scan, sort, print
    ...

if __name__ == "__main__":
    main()
