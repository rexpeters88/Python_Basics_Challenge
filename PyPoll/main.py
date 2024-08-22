import csv
# Path to the CSV 
csvpath = 'Resources/election_data.csv'
# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    next(csvreader)

