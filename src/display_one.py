#!/usr/bin/env python
"""Executable command that allows the user to input single datafile."""
import argparse
from utilities import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays the first n rows of a single dataframe."""
    fname = args.infile
    rows = args.num
    display_head(fname, rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a Single Dataset")
    parser.add_argument(
        "-n", "--num", type=int, help="# rows to display for a single dataset"
    )
    parser.add_argument(
        "infile", type=str, nargs="?", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
