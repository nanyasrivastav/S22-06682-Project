#!/usr/bin/env python
"""Command that allows the user to input whether they want to analyse
a single datafile or multiple datafiles.

The output is a stdout statement directing the user to execute
the necessary commands."""
import glob

print(
    f'\n    Datafiles in the uploaded directory include: \
    {glob.glob("./data/*.json")}'
)

num_files = input(
    "\n    The contents of how many files do you want displayed?\n\
    Enter 'S' for single file and 'M' for multiple files: "
)

if num_files == "S":
    print(
        "\n\n    Please run the 'display_one.py' command\n    \
        NOTE: Required arguments include path to datafile and \
        an optional argument includes entering the number of rows to print."
    )
else:
    print(
        "\n\n    Please run the 'display_all.py' command\n    \
        NOTE: Required arguments include path to all datafiles \
        and an optional argument includes entering the number of \
        rows to print for all inputted datafiles."
    )
