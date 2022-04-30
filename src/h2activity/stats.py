#!/usr/bin/env python
"""Command that displays simple statistics of the dataset(s).

Required arguments include path to datafile(s)."""
import argparse

from src.utilities import stats  # pylint: disable=import-error


def main(args):  # pylint: disable=redefined-outer-name
    """Displays simple statistics using pandas df.describe()"""
    for fname in args.infile:
        stats(fname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display simple statistics of inputted datafile(s)."
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input datafile path(s)"
    )
    args = parser.parse_args()
    main(args)
