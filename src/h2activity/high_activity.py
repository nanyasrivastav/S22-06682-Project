#!/usr/bin/env python
"""Command that extracts information from the dataset(s)
for well(s) with highest H2 activity.

The highest H2 activity is computed either from
(a) maximum rate of production of H2 (umolH_max_rate) or
(b) maximum value of H2 (umolH_max); depending on user's choice.

Required arguments include path to the datafile(s) and an
argument that allows the user to choose whether they would like
to extract data based on H2 rate (R) or H2 value (V).
"""
import argparse

from src.utilities import max_h2  # pylint: disable=import-error


def main(args):  # pylint: disable=redefined-outer-name
    """Finds well with highest H2 activity,
    extracts corresponding data and
    displays a summarized report."""
    for fname in args.infile:
        max_h2(fname, args.option)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display summarized report of well with high H2 activity"
    )
    parser.add_argument(
        "infile", type=str, nargs="*", default="-", help="Input datafile path(s)"
    )
    parser.add_argument(
        "-o",
        "--option",
        type=str,
        default="-",
        help="Input options that compute H2 activity; H2 Rate(R) or H2 Value(V)",
    )
    args = parser.parse_args()
    main(args)
