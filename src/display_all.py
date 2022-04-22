#!/usr/bin/env python
"""To display all the dataframes with a single command."""
import argparse
from read_data import display_head


def main(args):  # pylint: disable=redefined-outer-name
    """Displays the first n rows of user-inputted dataframe(s)."""
    for fname in args.infile:
        display_head(fname, args.num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To Display All Inputted Datasets")  # noqa: E501
    parser.add_argument(
        "-n", "--num", type=int, help="# rows to display for all datasets"
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
