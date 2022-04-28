#!/usr/bin/env python
"""Command that displays the contents of single or
multiple datafiles on the command line."""
import argparse
from utilities import stats


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
