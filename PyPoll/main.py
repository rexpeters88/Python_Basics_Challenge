import csv

total_votes = 0
candidate_list = []
votes = {}

# Path to the CSV 
csvpath = '/Users/rexpeters/Desktop/python-challenge/PyPoll/Resources/election_data.csv'
# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Count number of rows (1 row = 1 vote)
    for row in csvreader:
        total_votes += 1

        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1

#Print Title 
print("Election Results")
print("-------------------------")
#Print Total Votes in correct format
print(f"Total Votes: {total_votes}")
print("-------------------------")


# Calculate % votes from total votes stored in 'votes' dictionary
# x = candidate and y = total votes for that candidate
percentage_votes = {}
for x,y in votes.items():
    percentage = (y/total_votes) * 100
    rounded_percentage = round(percentage,3)
    percentage_votes[x] = rounded_percentage

    print(f"{x}: {rounded_percentage}% ({y} votes)")

print("-------------------------")

# Find the winner based on max popular votes from votes dictionary
# Key refers to each candidate in the diction which a value (total votes) is attatched to
# Max function iterates through each value to find the highest, and will return the key (the candidates name)
winner = max(votes, key=votes.get) 

print(f"Winner: {winner}")
print("-------------------------")


# Added script to save the result in the results.txt document saved in PyPoll Analysis Folder
output_path = '/Users/rexpeters/Desktop/python-challenge/PyBank/analysis/results.txt'
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    # Remade dictionary to export the percentage votes dictionary
    # Fixed exportation bug that was not allowing me to properly export (likely due to issues with indentation in the first calculation)
    percentage_votes_export = {}
    for z, f in votes.items():
        percentage_export = (f / total_votes) * 100
        rounded_percentage_export = round(percentage_export, 3)
        percentage_votes_export[z] = rounded_percentage_export
        file.write(f"{z}: {rounded_percentage_export}% ({f} votes)\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")


