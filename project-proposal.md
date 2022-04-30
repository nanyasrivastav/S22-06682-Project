# Project Proposal 

Objective: 
- Building a simple workflow with the help of command line utilities to (a) display the contents of the user's dataset(s) and (b) get useful summarized reports about it on Shell.

Motivation: 
- Switching back and forth between the terminal and ipynb notebook is sometimes a hindrance for simple workflows, 
hence, this project aims at developing a workflow on Shell that will allow the user to quickly read the contents of their dataset(s)
and analyze results obtained from their high throughput well plate experiments. 
- The initial development will focus on data obtained from the following experiment: “Photo Driven Hydrogen Evolution with Heterogeneous Metal Catalysts”.
For this experiment, the summarized report will contain information about which bimetallic composition/ well number 
gives the highest H2 activity from user-inputted experiment(s)/ dataset(s).

Note: In the datasets, H2 activity is reported either as the maximum production rate of H2 or maximum value (concentration) of H2 measured over time.

Overview:
- The user will be required to interact with Shell via a set of commands to perform the following tasks: 
1. pip install package containing command line utilities 
2. run a command to read the JSON data files uploaded by the user in a "data" directory and then 
display the first 'n' rows of the JSON data file (similar to how a dataframe is displayed on notebooks using Pandas)
– the purpose of this command is to allow the user to take a look at what their dataset contains, on Shell, instead of writing code to read JSON files on notebooks.
3. run a command to display the summarized report(s) as stdout or download the output onto their working directory as a .txt file.
4. run a command to display a report of simple statistics of the dataset(s)

- The summarized report in Task 3 would include the following information:
1. Based on the user's input, report high H2 activity as either the (a) maximum "Maximum value of H2 measured over time" (umolH_max) or 
(b) maximum "Maximum production rate of H2 measured over time" (umolH_max_rate) 
2. Report the well number/ well plate experiment that gives the highest H2 activity
3. Report the corresponding bimetallic composition and their respective concentrations 

Workflow Ideas for the Project Work:
1. Appropriate LICENSE will be included along with a setup.py file to install the package containing command-line utilities. 
2. Documentation describing the workflow on Shell will be provided in the README.md file along with metadata information.
3. Python scripts will be written to perform the commands mentioned in the previous section and will be made executable so that the user can directly run them from the working directory. 
4. pytest test files and GitHub actions workflows will be written to make sure that the package functions work as they are supposed to or raise an error if they do not.
5. Quality control using black, flake8 and pylint formatting will be automated on the package files using pre-commit hooks.

Timeline: 
- 4/18 - start writing python scripts
- 4/20 - in-class presentation
- 4/25 - pytest files/ get the workflow ready 
- 4/27 - in-class presentation/ add documentation
- 4/29 - project due