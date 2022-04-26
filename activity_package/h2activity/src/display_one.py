#!/usr/bin/env python
"""Command that allows the user to read a
single datafile on the command line."""
import argparse
from utilities import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays dataframe of the first n rows of a single datafile."""
    fname = args.infile
    rows = args.num
    display_head(fname, rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display contents of inputted single dataset."
    )  # noqa: E501
    parser.add_argument(
        "-n", "--num", type=int, help="# rows to display for single dataset"
    )
    parser.add_argument(
        "infile", type=str, nargs="?", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
