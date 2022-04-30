"""Module that provides functions to
(a) read datafile(s) and display its contents,
(b) output a summarized report of well plate experiment(s)
with highest H2 activity
(c) output simple statistics of the dataframe(s)."""
import sys
import pandas as pd  # pylint: disable=import-error


def display_head(fname, rows):
    """Reads datafile(s) and displays its first n rows."""
    if fname == "-":
        f_stdin = sys.stdin.read()  # use in piping commands
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    print(f"\n{data.head(rows)}")


def max_h2(fname, option):
    """Reads datafile(s) and displays the maximum H2 rates/ values,
    the corresponding well number, bimetallic composition and respective
    concentrations."""
    if fname == "-":
        f_stdin = sys.stdin.read()  # use in piping commands
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    if option == "R":  # to extract information based on rate
        rate_hy = data["umolH_max_rate"].max()
        high_activity_rate = data.query("umolH_max_rate == @rate_hy")
        print(f"\n   Maximum production rate of H2: {rate_hy} umol/time")
        print(f"   Well # : {high_activity_rate.index.tolist()}")
        print(f"   Bimetallic Composition: {high_activity_rate.columns.values[:2]}")
        print("   Concentration of metals:")
        for i in list(high_activity_rate.iloc[:, :2]):
            conc = high_activity_rate[i].tolist()
            print(f"   {conc[0]} umol")
    elif option == "V":  # to extract information based on value
        value_hy = data["umolH_max"].max()
        high_activity_value = data.query("umolH_max == @value_hy")
        print(f"\n   Maximum value of H2: {value_hy} umol")
        print(f"   Well # : {high_activity_value.index.tolist()}")
        print(f"   Bimetallic Composition: {high_activity_value.columns.values[:2]}")
        print("   Concentration of metals:")
        for i in list(high_activity_value.iloc[:, :2]):
            conc = high_activity_value[i].tolist()
            print(f"   {conc[0]} umol")
    else:
        print("\n    INVALID OPTION ENTERED!\n")


def stats(fname):
    """Reads datafile(s) and displays simple statistics."""
    if fname == "-":
        f_stdin = sys.stdin.read()
        data = pd.read_json(f_stdin)
    else:
        data = pd.read_json(fname)

    print(data.describe())
