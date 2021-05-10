# Election_Analysis

## Overview of Election Audit

The purpose of this project was to help Tom audit the election votes within a congressional district in Colorado. The goal is to use a python script to present total votes, total county votes, total candidate votes, and the winner of the election in a text file to present to Tom and his boss. 

## Election Audit Results

The script written to audit this election can be found here: [PyPoll Script](https://github.com/fadlnabbouh/Election_Analysis/blob/main/PyPoll_Challenge.py). A report in a txt file can be found here: [analysis](https://github.com/fadlnabbouh/Election_Analysis/blob/main/analysis/election_analysis.txt). 

The results of the Election are as follows: 

- Total Votes Cast: 369,711. 
- County Votes: 
	- Jefferson: 38,855 (10.5%)
	- Denver: 306,055 (82.8%)
	- Arapahoe: 24,801 (6.7%)
- County with most votes: Denver
- Candidate Votes: 
	- Charles Casper Stockham: 85,213 (23.0%)
	- Diana DeGette: 272,892 (73.8%)
	- Raymon Anthony Doane: 11,606 (3.1%)
- Winner of the Election: 
	- Candidate: Diana DeGette
	- Total Votes: 272,892
	- Vote Percentage: 73.8%

A screenshot of how the script appears in terminal after running can be found here: ![Screenshot]().

## Election Audit Summary 

In summary, I managed to write a script that automatically analyzed election results for the Jefferson, Denver, and Arapahoe county. 

This script can be used, with modification, in larger elections that span multiple counties and potentially entire states. Because the script automatically notes new county names, no adjustment would be needed if the script was used to analyze more counties. 

It can, however, be modified to include an analysis of more geographic or demographic detail. For example, if the election committee included data on which states a county is in, as well as demographic information including sex, race, and socioeconomic status of each county's constitutents, the script can be modified to analyze the vote breakdown of these various demographics. In addition, I can also adjust the script to determine each county's vote percentage per candidate, providing analysis on which candidates are more heavily favoured in which county.
