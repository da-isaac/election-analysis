# Election Analysis
Creation of algorithm to help calculate election results for congressional, senatorial, and local elections 

## Overview of Project

### Purpose
The client, Tom, is a Board of Education member for Colorado who has requested help developing an automated program that can help summarize the election results within a specific area or district. 
The program will be able to report total votes per candidate and county, and determine the winner of the election.

## Results
* How many votes were cast in this congressional election?
    369,711

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    ![County](/Resources/County_Results.PNG)

* Which county had the largest number of votes?
    Denver

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    ![Candidate](/Resources/Candidate_Results.PNG)

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    ![Winner](/Resources/Candidate_Results.PNG)


## Summary
This code provides an adequate base that can be used going forward for similar elections or, with some modifications, other types of elections. The first modification I recommend is adding a dictionary into the script that allows a "congressional district" value to be used. In order to be used properly, the dataset would also need a column specifying which congressional district the votes came from so they could be properly summarized. Doing this would allow for election summaries to be run state-wide, regardless of the number of districts needing analyzed.
The second modification I recommend is adding a dictionary that allows a "state" value to be used. Again, the dataset would require a state value to be included for the script to run properly, but that would open up this program's use-case to be nationwide. 