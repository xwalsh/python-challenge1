import csv
import os

# path
csvpath = '/Users/xavier/Documents/GitHub/python-challenge1/PyPoll/Resources/election_data.csv'

# Confirm file being read
print('File:', csvpath)

# Initialize vote counter and dictionary to store candidate votes
totalVotes = 0
votescandidates = {}

# Open and read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV
    for row in csvreader:
        totalVotes += 1
        candidate = row[2].strip()
        if candidate not in votescandidates:
            votescandidates[candidate] = 1
        else:
            votescandidates[candidate] += 1

# Write election results 
with open('Election_Data_Results.txt', 'w') as file:
    print("Election Results")
    file.write("Election Results\n")
    
    print("---------------------------")
    file.write("---------------------------\n")

    print(f"Total Votes: {totalVotes}")
    file.write(f"Total Votes: {totalVotes}\n")

    print("---------------------------")
    file.write("---------------------------\n")

    # Display and record each candidate's results
    for candidate, votes in votescandidates.items():
        percentage = votes / totalVotes
        print(f"{candidate}: {percentage:.3%} ({votes})")
        file.write(f"{candidate}: {percentage:.3%} ({votes})\n")

    print("---------------------------")
    file.write("---------------------------\n")

    # Determine the winner
    winner = max(votescandidates, key=votescandidates.get)
    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}\n")

