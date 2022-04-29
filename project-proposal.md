# Project Proposal 

Objective: 
- Building command line utilities to get a summarized report about the user’s datasets on Shell.

Overview: 
- The main idea of this project is to build command line utilities on Shell that can be used to display the user's dataset(s) and 
read/ download its summarized report.
- Switching back and forth between the terminal and ipynb notebook is sometimes a hindrance for simple workflows, 
hence, this project aims at developing a workflow on Shell that will allow the user to quickly analyze results obtained from 
their high throughput experiments.
- The initial development will focus on three datasets obtained from the following experiment: 
“Photo Driven Hydrogen Evolution with Heterogeneous Metal Catalysts”. 

- The user will be required to interact with Shell via a set of commands to perform the following tasks: 
1. pip install package containing command line utilities 
2. run a command to read the JSON data files uploaded by the user 
3. run a command to display the first 'n' rows of the JSON data file (similar to how a data frame is displayed on Deepnote using Pandas)
– the purpose of this command is to allow the user to take a look at what their dataset contains, on Shell, instead of writing code to read JSON files on ipynb notebooks.
4. run a command to either display the summarized report as stdout or download the report onto their working directory as a .txt file.
– this command could have options to either look at the simple report as stdout or download it as pdf or txt file onto the desktop/ Deepnote folder

The summarized report in Task 4 would include the following information:
1. Input options from the user to either (a) report the maximum "Max value of H2" measured over time (umolH_max) or 
(b) report the maximum "Max production rate of H2" over time (umolH_max_rate) 
2. Report the corresponding bimetallic composition and their respective concentrations 
3. Compare the above-extracted data and tell the user which experiment or bimetallic catalyst composition has the highest activity for H2 production !!!!!!

Workflow Ideas:
1. Appropriate LICENSE.md files would be included along with a setup.py file to install the package containing command-line utilities. 
2. Documentation describing the Shell workflow will be provided in the README.md file along with metadata information. !!!!!!!!!!!!1
3. A requirements.txt file with common python libraries such as pandas (to read JSON files and perform analysis on the data frame) will be included. !!!!!!!!!!!
4. Python scripts will be written to perform the tasks mentioned in the previous section and will be made executable so that the user can directly run them as commands. 
5. Test files for pytest and GitHub actions will be written to make sure that the python functions work well and raise an error if it doesn’t.
It could also be used to ensure that the user inputs only JSON files, or raises errors if the JSON file does not contain columns in the same format as the package scripts require it to be in.
6. Quality control will be automated on the package (pre-commit hooks) to produce a high-quality package. 

Timeline: 
- 4/18 - start writing python scripts
- 4/20 - in-class presentation
- 4/25 - pytest files/ get the workflow ready 
- 4/27 - in-class presentation/ add documentation
- 4/29 - project due