#!/usr/bin/env python
"""Command that displays the first n rows of datafile(s).

Required arguments include path to datafile(s).
Optional argument include number of rows to display."""
import argparse

from src.utilities import display_head  # pylint: disable=import-error


def main(args):  # pylint: disable=redefined-outer-name
    """Displays first n rows of dataframe(s)."""
    for fname in args.infile:
        display_head(fname, args.rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Displays first n rows of user-inputted datafile(s)."
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input datafile path(s)"
    )
    parser.add_argument(
        "-r", "--rows", type=int, help="# rows to display for dataframe(s)"
    )
    args = parser.parse_args()
    main(args)
