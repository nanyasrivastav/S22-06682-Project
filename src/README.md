# ⚗️ H2 Activity Package 

This readme file contains detailed information about the contents of the package and the different command line utilities it offers. 
A step-by-step tutorial, with examples of how to run a simple workflow on the command line, has also been included with this file. 

The initial development of this package focuses on analysing data obtained from high throughput well plate experiments, in particular, for experimental work titled
“Photo Driven Hydrogen Evolution with Heterogeneous Metal Catalysts”. Each high throughput experiment generates 96 data points, hence a simple workflow to perform 
quick analysis on the data is what this package aims to provide to the user. 

A summarized report containing information about the well plate experiment with highest H2 activity and its corresponding bimetallic properties 
can be obtained with a single command line. The user can also download and store these results onto their working directory as .txt files, 
this option could be useful for future analysis or comparison of results. Along with this, the package provides command line utilties to display the contents of the dataframes 
and some simple statistical results using the pandas library.

## 🌳 Package Structure

The following structure is a list of the main directories and files present in this package. 
It can be obtained by running the following commands on Shell. 

    sudo apt-get update

    sugo apt-get install tree
    
    tree -F src

Output of the tree command: 

    src
    ├── h2activity/
    │   ├── data_examples/
    │   │   ├── AucolCurow.json
    │   │   ├── AucolSnrow.json
    │   │   └── PdcolPbrow.json
    │   ├── display.py
    │   ├── high_activity.py
    │   ├── __init__.py
    │   ├── start.py
    │   └── stats.py
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.md
    ├── setup.py
    ├── tests/
    │   ├── test_fail.py
    │   └── test_path.py
    └── utilities.py

- The setup.py file indicated that the module/ package is pip installable.
- The LICENSE file contains details of the GNU General Public License terms and conditions. 
- The tests contains test files that run on GitHub Actions and ensure the proper functioning of the package.
- The utilities.py module contains definition of functions imported by the package commands.
- The h2activity/ directory is the name of the package and contains several .py scripts that are executable commands.
- The data_examples/ directory contains example JSON datafile that are inlcuded with the package for the user to practice on.

## 📋 Metadata

The initial development of this package deals with datasets that contain data from 3 experiments. 
The experiments are 96 well plate experiments, where each well contains a unique combination (or concentrations) of input components. 
The output metric of the experiment is hydrogen evolution data in umolH. 

Data:
The data is in JSON file format and that package requires user-inputted datafiles to be in the same format. 
The dataframe has 96 rows corresponding to the 96 wells. The first 5 columns are inputs in the wells, and the last 4 columns have the output information. 

Inputs:
The inputs contain 2 metals, TEOA, DMSO, and photosensitizer. All values are concentrations in umol. 

Outputs:
The umolH_max is the maximum value of H2 measured over time, while the umolH_max_rate is the maximum production rate of H2 measured over time.
The maximum value of umolH_max and umolH_max_rate define maximum H2 activity and can be used to identify the well plate experiment/ well number and its
corresponding bimetallic properties.
umolh and time are the time series data.

## ⏭ Workflow tutorial along with brief explanation of the commands
Step 1: pip install the package onto the local repository or the working directory

    pip install src/

Step 2: Once the package has been setup; start the workflow by entering the following command on the working directory. The purpose of this command is to allow the user to explore the different 
command line utilities inlcuded with the package. It is an interactive command line utility that takes the user's choices into consideration and outputs directions to help the user navigate 
through the workflow.

    start.py

Note: This step can be skipped if needed. It is just provided as a starting point.

Step 3: Output the first "n" rows of the dataset(s) on Shell. This command uses the pandas library to read and display the contents of the JSON datafiles.
It can be executed in the following ways to give the user some flexibility on the command line.

A simple command that takes the path of single datafile as its argument. The output of this command is the contents of the dataframe (all rows and columns). 

    display.py ./data/AucolCurow.json 

If the output of the entire dataframe is not required at any stage, add the optional argument to display the first "n" rows of the dataset. 
The example below would output the first 5 rows of the dataframe.

    display.py ./data/AucolCurow.json -r 5

To output the contents of several dataframes, add paths to several datafiles as space separated arguments and/ or add the optional argument to display the first "n" rows of 
all of the user-inputted datasets.

    display.py ./data/AucolCurow.json ./data/AucolSnrow.json 

    display.py ./data/AucolCurow.json ./data/AucolSnrow.json -r 3

Note: This version of the package will display the same number of rows for all datafiles. Later development can focus on providing arguments that take in different number of rows to display for
different dataframes.

Step 4: To get a summarized report of the dataset(s), use this command and add the path(s) to the datafile(s) along with a required argument that takes the option to compute either the 
maximum rate of H2 production (R) or the maximum value of H2 (V) measured over time. Based on the user's choice, the well plate experiment or well number with the highest H2 activity 
will be reported along with information of the corresponding bimetallic composition and concentration.

To find the well plate experiment/ well number with highest H2 activity in the AucolCurow.json datafile based on maximum rate of H2 production.

    high_activity.py ./data/AucolCurow.json -o R

To find the well plate experiment/ well number with highest H2 activity in the AucolSnrow.json datafile based on maximum value of H2.

    high_activity.py ./data/AucolSnrow.json -o V

To download the results of the analysis onto the working directory as a text file. 

    high_activity.py ./data/AucolCurow.json -o R > report.txt

To find well plate experiments/ well numbers with highest H2 activity for several datafiles. This could be useful for comparison of results between 2 or more high throughput experiments.

    high_activity.py ./data/AucolCurow.json ./data/AucolSnrow.json -o R 

Step 5: To get simple statistics of the dataframes(s) as stdout report(s) or downloaded as a text file. This command uses the df.describe() function in pandas. 
Hence, the following information will be outputted: count, mean, min, max, std deviation etc. 

    stats.py ./data/AucolCurow.json

    stats.py ./data/AucolSnrow.json ./data/AucolCurow.json

    stats.py ./data/AucolCurow.json > statistics.txt
