# import libraries
import os
import csv
import sys

# Set the path to retrieve the voting records file for PyPoll
pypoll_csv = os.path.join("..", "Starter_Code", "PyPoll", "Resources", "election_data.csv")


# Empty lists to hold the polling data
ballot_id = []
county = []
candidate = []

# Open csv file and fill lists
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    pypoll_headers = next(csv_reader)

    for row in csv_reader:
        ballot_id.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))


# Calculate the Key Metrics: Total Votes Cast, a List of Candidates, Percentage of Votes for Each, 
# Total Votes for each, the Winner
total_votes = len(ballot_id)                                                
unique_candidates = list(set(candidate))
unique_candidates.sort()

# Dictionaries to hold votes
vote_count_dict = {key: 0 for key in unique_candidates}
vote_percent_dict = {key: 0 for key in unique_candidates}

# Count the votes
for contender in candidate:
    vote_count_dict[contender] += 1

# Variables to keep track of the winner and their count
winner_count = 0
winner = ""

# Calculate the percentage of votes each candidate received and determine the winner 
for key in vote_count_dict:
    vote_percent_dict[key] = vote_count_dict[key]/total_votes
    if vote_count_dict[key] > winner_count:
        winner = key                                                     
        winner_count = vote_count_dict[key]


# Print results to Terminal
print("")
print("Election Results")
print("")
print("--------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("--------------------------")
print("")
print(f"{unique_candidates[0]}: {round(100 * vote_percent_dict[unique_candidates[0]], 3)}% ({vote_count_dict[unique_candidates[0]]})")
print("")
print(f"{unique_candidates[1]}: {round(100 * vote_percent_dict[unique_candidates[1]], 3)}% ({vote_count_dict[unique_candidates[1]]})")
print("")
print(f"{unique_candidates[2]}: {round(100 * vote_percent_dict[unique_candidates[2]], 3)}% ({vote_count_dict[unique_candidates[2]]})")
print("")
print("--------------------------")
print("")
print(f"Winner: {winner}")
print("")

# Write and export the results to a text file: pypoll_vote_results.txt
# "https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file"
f = open("pypoll_vote_results.txt", 'w')
sys.stdout = f

print("")
print("Election Results")
print("")
print("--------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("--------------------------")
print("")
print(f"{unique_candidates[0]}: {round(100 * vote_percent_dict[unique_candidates[0]], 3)}% ({vote_count_dict[unique_candidates[0]]})")
print("")
print(f"{unique_candidates[1]}: {round(100 * vote_percent_dict[unique_candidates[1]], 3)}% ({vote_count_dict[unique_candidates[1]]})")
print("")
print(f"{unique_candidates[2]}: {round(100 * vote_percent_dict[unique_candidates[2]], 3)}% ({vote_count_dict[unique_candidates[2]]})")
print("")
print("--------------------------")
print("")
print(f"Winner: {winner}")
print("")

f.close()
