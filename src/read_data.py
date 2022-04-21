"""Using Pandas or stdin to read JSON datafile(s)."""
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
