#!/usr/bin/env python
"""Executable command that allows the user to input multiple datafiles."""
import argparse
from utilities import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays the first n rows of multiple user-inputted dataframe(s)."""
    for fname in args.infile:
        display_head(fname, args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display All Inputted Datasets"
    )  # noqa: E501
    parser.add_argument(
        "-n", "--num", type=int, help="# rows to display for all datasets"
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
