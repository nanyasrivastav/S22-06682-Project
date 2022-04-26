#!/usr/bin/env python
"""Command that allows the user to read
multiple datafiles on the command line."""
import argparse
from utilities import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays dataframe(s) of the first n rows of
    user-inputted datafiles(s)."""
    for fname in args.infile:
        display_head(fname, args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display contents of inputted multiple datasets."
    )  # noqa: E501
    parser.add_argument(
        "-n", "--num", type=int, help="# rows to display for all datasets"
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
