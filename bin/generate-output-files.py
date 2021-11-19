#!/usr/bin/env python
import csv
import json
import logging
import sys

from pathlib import Path

logger = logging.getLogger(__name__)

root_dir = Path(__file__).parent.parent


def main(input_file=None):
    if input_file is None:
        file_list = list((root_dir / "source").glob("*.csv"))
        if len(file_list) > 1:
            logger.error("Multiple input files found. Quitting.")
            sys.exit(10)
        input_file = file_list[0]

    with open(input_file, 'rt', encoding="utf-8-sig") as csvfile:
        data = list(csv.DictReader(csvfile))

    with open(root_dir / "qlacref_authorities/records.json", 'wt') as jsonfile:
        json.dump(data, jsonfile, indent=2)


if __name__ == "__main__":
    main()
