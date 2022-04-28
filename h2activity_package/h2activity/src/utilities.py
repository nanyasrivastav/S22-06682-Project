"""Providing functions to read data, display its contents,
and output the maximum umolH_max_rate or umol_H based on user input.
"""
import sys
import pandas as pd


def display_head(fname, rows):
    """Reads datafile(s) and displays its first n rows."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    print(f"\n{data.head(rows)}")


def max_h2(fname, option):
    """Reads datafile(s) and displays the maximum H2 rates/ values,
    the correspoding well number, bimetallic composition and its respective
    concentrations."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    if option == "R":
        rate_hy = data["umolH_max_rate"].max()
        high_activity_rate = data.query("umolH_max_rate == @rate_hy")
        print(f"\n   Maximum production rate of H2: {rate_hy} umol/time")
        print(f"   Well # : {high_activity_rate.index.tolist()}")
        print(
            f"   Bimetallic Composition:\
        {high_activity_rate.columns.values[:2]}"
        )
        print("   Concentration of metals:")
        for i in list(high_activity_rate.iloc[:, :2]):
            conc = high_activity_rate[i].tolist()
            print(f"   {conc[0]} umol")
    elif option == "V":
        value_hy = data["umolH_max"].max()
        high_activity_value = data.query("umolH_max == @value_hy")
        print(f"\n   Maximum value of H2: {value_hy} umol")
        print(f"   Well # : {high_activity_value.index.tolist()}")
        print(
            f"   Bimetallic Composition:\
        {high_activity_value.columns.values[:2]}"
        )
        print("   Concentration of metals:")
        for i in list(high_activity_value.iloc[:, :2]):
            conc = high_activity_value[i].tolist()
            print(f"   {conc[0]} umol")


def stats(fname):
    """Displays statistical data of the dataframe(s)."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    print(data.describe())
