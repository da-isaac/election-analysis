# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the elecction based on popular vote

import csv
import os

# Read data by direct path to the file

# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

    #TODO: perform analysis
    print(election_data)

# Read data by indirect path to the file

# Assign a variable to the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

    #TODO: perform analysis
    print(election_data)