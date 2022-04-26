#!/usr/bin/env python
"""Command that allows the user to input whether they want to analyse
a single datafile or multiple datafiles.

The output is a stdout statement directing the user to execute
the necessary commands."""
import glob

print(
    f'\n    Datafiles in the uploaded directory include:\
    {glob.glob("./data/*.json")}'
)

num_files = input(
    "\n    The contents of how many files do you want displayed?\n\
    Enter 'S' for single file and 'M' for multiple files: "
)

if num_files == "S":
    print(
        "\n    Please run the 'display_one.py' command\n\n\
    NOTE: Required arguments include path to datafile and\n\
    an optional argument includes entering the number of rows to print."
    )
elif num_files == 'M':
    print(
        "\n    Please run the 'display_all.py' command\n\n\
    NOTE: Required arguments include path to all datafiles\n\
    and an optional argument includes entering the number of\n\
    rows to print for all inputted datafiles."
    )
else:
    print("\n\n    INVALID OPTION ENTERED\n")
