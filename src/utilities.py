"""Providing functions to read data, display its contents,
and output the maximum umolH_max_rate or umol_H based on user input.
"""
import sys
import pandas as pd


def display_head(fname, rows):
    """Reads a datafile and displays its first n rows."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    print(data.head(rows))


def max_value(fname):
    """Reads a datafile and displays the maximum values."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    maxloc = input("Enter rate/ value: ")

    if maxloc == "rate":
        rate_hy = data["umolH_max_rate"].max()
        high_activity_rate = data.query("umolH_max_rate == @rate_hy")
        print(rate_hy)
        print(high_activity_rate.iloc[:, :5])
    else:
        value_hy = data["umolH_max"].max()
        high_activity_value = data.query("umolH_max == @value_hy")
        print(value_hy)
        print(high_activity_value.iloc[:, :5])
