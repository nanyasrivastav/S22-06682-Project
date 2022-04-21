import pandas as pd
import sys 

def display_head(fname, rows):
    if fname == '-':
        f = sys.stdin.read()
        df = pd.read_json(f)
    else:
        df = pd.read_json(fname)
        
    print(df.head(rows))

