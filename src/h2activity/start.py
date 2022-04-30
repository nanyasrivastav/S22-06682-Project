#!/usr/bin/env python
"""Command that first displays the path of all the .json datafiles
(uploaded by the user) in the "data" directory and then prompts the user
to input whether they want the contents of a single datafile or
multiple datafiles displayed on Shell.

The command also prompts the user to input whether they would
like to see an example of how the commands run.

The purpose of this command is to act as a starting point and
direct the user to start a workflow on Shell and run commands 
included with the package."""
import glob

print(
    f'\n    Datafiles in the uploaded directory include:\
    {glob.glob("./data/*.json")}'
)

num_files = input(
    "\n    How many files/ experiments do you want to analyze?\n\
    Enter 'S' for single and 'M' for multiple: "
)

if num_files == "S":
    print(
        "\n    Run 'display.py' to display first n rows of datafile\n\
    Run 'high_activity.py' to find Well with highest H2 activity in experiment\n\
    Run 'stats.py' to display simple statistics of datafile"
    )

    ans = input(
        "\n    Do you want to see an example of how these commands work? (y/n) "
    )
    if ans == "y":
        print(
            "\n    Type the following commands on the command line:\n\n\
        display.py ./path/to/file -r 5 \n\
        high_activity.py ./path/to/file -o R \n\
        stats.py ./path/to/file\n"
        )
    elif ans == "n":
        print("\n    Please continue.")
    else:
        print("\n    INVALID OPTION ENTERED!\n")

elif num_files == "M":
    print(
        "\n    Run 'display.py' to display first n rows of the datafiles\n\
    Run 'high_activity.py' to find Well with highest H2 activity in experiments\n\
    Run 'stats.py' to display simple statistics of datafiles"
    )

    ans = input("\n    Do you want to see an example of how commands work? (y/n) ")
    if ans == "y":
        print(
            "\n    Type the following command on the command line:\n\n\
        display.py ./path/to/file_one.json ./path/to/file_two.json -r 3 \n\
        high_activity.py ./path/to/file_one.json ./path/to/file_two.json -o V \n\
        stats.py ./path/to/file_one.json ./path/to/file_two.json\n"
        )
    elif ans == "n":
        print("\n    Please continue.")
    else:
        print("\n    INVALID OPTION ENTERED!\n")

else:
    print("\n    INVALID OPTION ENTERED!\n")
