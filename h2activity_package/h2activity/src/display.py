#!/usr/bin/env python
"""Command that displays the contents of single or
multiple datafiles on the command line."""
import argparse
from utilities import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays dataframe(s) of the first n rows of
    user-inputted dataframe(s)."""
    for fname in args.infile:
        display_head(fname, args.rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display contents of inputted datafile(s) as dataframes."
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input datafile path(s)"
    )
    parser.add_argument(
        "-r", "--rows", type=int, help="# rows to display for dataframe(s)"
    )
    args = parser.parse_args()
    main(args)
