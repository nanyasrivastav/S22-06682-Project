#!/usr/bin/env python
"""Command that allows the user to input whether they want to analyse
a single datafile or multiple datafiles.

The output is a stdout statement directing the user to execute
the necessary commands."""

num_files = input("\n    How many files do you want to analyse?\n    Enter 'S' for single file and 'M' for multiple files: ")

if num_files == "S": 
    print("\n\n    Please run the 'display_one.py' command \n    NOTE: Required arguments include path to datafile and optional argument includes entering the number of rows to print.")
else: 
    print("\n\n    Please run the 'display_all.py' command \n    NOTE: Required arguments include path to all datafiles and optional argument includes entering the number of rows to print for all inputted datafiles.")