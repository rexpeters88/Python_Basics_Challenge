import csv

# Path to the CSV 
csvpath = 'Resources/budget_data.csv'

# Initialize variables
total_months = 0
dates = []
net_total = 0
previous_profit_loss = None
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    next(csvreader)
    
    # Iterate through rows
    for row in csvreader:
        # Increment total months
        total_months += 1
        # Append date to the list
        dates.append(row[0])  # Assuming date is in the first column

        profit_loss = int(row[1])  
        net_total += profit_loss

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        previous_profit_loss = profit_loss

# Calculate the total number of unique months
unique_months = len(dates)

# Calculate Average Change
avg_change = sum(changes)/ len(changes)
# Round to 2 decimals 
rounded_avg_change = round(avg_change, 2)

# Print Values
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {unique_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${rounded_avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


output_path = 'analysis/results.txt'
with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-------------------------\n")
    textfile.write("Total Months: {unique_months}\n")
    textfile.write("Total: ${net_total}\n")
    textfile.write("Average Change: ${rounded_avg_change}\n")
    textfile.write("Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write("Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


