#!/usr/bin/env python
"""Executable command that allows the user to input whether they need
to extract experimental information about umolH_max_rate or umolH_max
from the user-inputted datafile.
"""
import argparse
from utilities import max_value


def main(args):  # pylint: disable=redefined-outer-name
    """Extracts data of experiment with highest H2 activity."""
    fname = args.infile
    max_value(fname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display High Activity")
    parser.add_argument(
        "infile", type=str, nargs="?", default="-", help="Input file name(s)"
    )
    args = parser.parse_args()
    main(args)
