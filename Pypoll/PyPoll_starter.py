# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

#Import necessary modules
import csv
import os

#Files to load and output (update with correct file paths)
input_file = os.path.join("Resources", "election_data.csv")  # Input file path
output_file = os.path.join("analysis", "election_analysis.txt")  # Output file path

#Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

#Define lists and Dictionaries to track candidate names and vote counts
candidate_votes = {}

#winning candidate and winning Count Tracker
winning_candidate = ""
winning_count = 0

#open the csv file and process it
with open(input_file) as election_data:
    reader = csv.reader(election_data)
    
    #Skip the header row    
    header = next(reader)
    
    #loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name]=0
    
    
    #increment the total vote count for each row
    
    #Get the candidate's name from the row
        candidate_votes[candidate_name] += 1

#print the total vote count (to terminal)
with open(output_file,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------\n"
    )
 # Write the total vote count to the text files  
    print(election_results)
    txt_file.write(election_results)

#loop through the candidates to determine vote percentages and identify the winner

#get the vote count and calculate the percentage
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100

#update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
#print a loading indication (for large datasets)
#print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}:{vote_percentage:3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

#generate and print the winning summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n"
    )
#save the winning candidate summary to the text file
    print(winning_summary)
    txt_file.write(winning_summary)



    
