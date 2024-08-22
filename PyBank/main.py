import csv

# Path to the CSV 
csvpath = 'Resources/budget_data.csv'

# Initialize variables
total_months = 0
dates = []
net_total = 0
previous_profit_loss = None # Neccesary to account for having nothing to compare the first value to
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    # Iterate through rows
    for row in csvreader:
        # Add total months
        total_months += 1
        # Append date to the list
        dates.append(row[0])  

        profit_loss = int(row[1])  
        net_total += profit_loss
        
        # Calculate differences between each profit/loss and add value to array
        if previous_profit_loss is not None: # 'None' allows us to skip the first value since there is no prior value to compare it to
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Compare each change to following change to find largest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Update proft/loss for next row
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


