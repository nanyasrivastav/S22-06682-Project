#!/usr/bin/env python
"""This command first displays the path of all the .json datafiles
(uploaded by the user) in the "data" directory and then prompts the user
to input whether they want the contents of a single datafile or
multiple datafiles displayed on Shell.

The command also prompts to user to input whether they would
like to see an example of how the commands run.

The purpose of this command is to direct the user
to execute a command that will display the contents datafiles."""
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
    print("\n    Please run the 'display.py' command\n")

    ans = input(
        "\n    Do you want to see an example of \
    how the command works? (y/n) "
    )
    if ans == "y":
        print(
            "\n    Type the following command on the command line:\n\n\
        display.py ./path/to/file -r 5\n"
        )
    elif ans == "n":
        print("\n    Please continue.")
    else:
        print("\n    INVALID OPTION ENTERED!\n")

elif num_files == "M":
    print("\n    Please run the 'display.py' command\n")

    ans = input(
        "\n    Do you want to see an example of \
    how the command works? (y/n) "
    )
    if ans == "y":
        print(
            "\n    Type the following command on the command line:\n\n\
        display.py ./path/to/file_one.json ./path/to/file_two.json \
        ./path/to/file_three.json -r 5\n"
        )
    elif ans == "n":
        print("\n    Please continue.")
    else:
        print("\n    INVALID OPTION ENTERED!\n")

else:
    print("\n    INVALID OPTION ENTERED!\n")
