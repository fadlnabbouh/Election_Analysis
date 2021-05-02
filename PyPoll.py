
#Retrieve Data
#Add dependencies
import csv
import os

#Assign variable to load a file
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file 

#initialize total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    #To do: read and analyze the data here

    file_reader = csv.reader(election_data)
    #Read and print header row 

    headers = next(file_reader)

    for row in file_reader:
        
        #add to total vote count
        total_votes += 1
        
        #retrieve candidate name from each row
        candidate_name= row[2]
        
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            #begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]     
    #calculate percentage
    vote_percentage = float(votes)/ float(total_votes) * 100
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    if  (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
winning_candidate_summary=(
     f"------------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"--------------------------------\n")
print(winning_candidate_summary)





#1. Retrieve total number of votes cast 
#2. Retrieve list of candidates with at least one vote
#3. Retrieve total number of votes each candidate received
#4. Retrieve total number of votes cast
#5. Retrieve percentage of votes each candidate received