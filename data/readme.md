This dataset contains data from 3 experiments. The experiments
are 96 well plate expeirments where each well contains a 
unique combination (concentrations) of input components. The 
output metric is hydrogen evolution data in umolH. 

Data:
The data is in json files that can be read into pandas with 
read_json(filepath). The dataframe has 96 rows corresponding to 
96 wells. The first 5 columns are inputs in the wells, and the 
last 4 columns have the output information. 

Inputs:
The inputs contain 2 metals, TEOA, DMSO, and photosensitizer. 
The values there are concentrations. 

Outputs:
The output are micromoles of H2. The max umolH is the max value 
of H2 measured over the time, the max rate is the maximum production
rate over the time, and the umolh and time are the time series data.

Possible projects:
Theoretically, you should create a package that is built with one of 
the datasets, and you should be able to test it on the other 2 
datasets. 

Regression analysis for inputs to predict outputs 
Analysis of time series data - smoothing, incubation time (the graphs 
are flat before H2 production starts), correlations between max rate
and max H2. 
Generate reports with metadata of concentration ranges, comparisons
of best and worst performing wells. 
