#!/usr/bin/env python
"""Command that extracts experimental information of H2 activity
in terms of maximum rate of production of H2 or maximum value of
H2 depending on user input.

The command requires the user to input the path of the datafile(s)
as an argument and an option that chooses whether they would like
to extract data based on rate or value.
"""
import argparse
from utilities import max_h2


def main(args):  # pylint: disable=redefined-outer-name
    """Extracts data of experiment(s) with highest H2 activity."""
    for fname in args.infile:
        max_h2(fname, args.option)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display High Activity")
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input datafile path(s)"
    )
    parser.add_argument(
        "-o",
        "--option",
        type=str,
        default="-",
        help="Input options H2 Rate(R) or H2 Value(V)",
    )
    args = parser.parse_args()
    main(args)
