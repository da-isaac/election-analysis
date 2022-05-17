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
##file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
##with open(file_to_load) as election_data:

    #TODO: perform analysis
##    print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = 'analysis/election_analysis.txt'
##file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Add a header line and line separator
    txt_file.write("Counties in the election\n")
    txt_file.write("-------------------------\n")

    # Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

