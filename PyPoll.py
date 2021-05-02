
##Assign a variable for the file to load and the path
#import csv

#file_to_load = 'Resources/election_results.csv'

##Open the election results and read the file

#election_data = open(file_to_load, 'r')

#To do: perform analysis

#Close the file 

#election_data.close()

#Open the file using 'with'

#with open(file_to_load) as election_data:
#    print(election_data)

#indirect method

#import os
#file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_data:
#    print(election_data)

#create filename variable
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#write data to the file
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")
#outfile.close()
#Cleaner: 

#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")





#pseudocode

#Retrieve Data
#Add dependencies
import csv
import os

#Assign variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file 

with open(file_to_load) as election_data:
    #To do: read and analyze the data here

    file_reader = csv.reader(election_data)
    #print each row in the CSV file
    #for row in file_reader:
    #    print (row)
    #Read and print header row 

    headers = next(file_reader)
    print(headers)
    
#1. Retrieve total number of votes cast 
#2. Retrieve list of candidates with at least one vote
#3. Retrieve total number of votes each candidate received
#4. Retrieve total number of votes cast
#5. Retrieve percentage of votes each candidate received