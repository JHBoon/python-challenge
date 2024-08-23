# Import read and open file with total months
import os

import csv
 #set variables
total_months = 0
total_profit = 0
profit_losses = []
dates = []
greatest_increase = float('-inf')
greatest_increase_date = ""
greatest_decrease = float('inf')
greatest_decrease_date = ""

print("Financial Analysis")
print("----------------------------")

# Open the CSV file
with open('budget_data.csv', 'r') as file:  
    total_rows_date_column = 0
    total_months = set()
    
    # Read the header to get the index of the 'date' column
    header = file.readline().strip().split(',')
    date_column_index = header.index('Date')
    
    # Iterate over the remaining lines in the file
    for line in file:
        columns = line.strip().split(',')
        if len(columns) > date_column_index:  # Check if the 'date' column exists in the current row
            date_value = columns[date_column_index]
            if  date_value:  # Check if the 'date' column value is not empty
                total_months.add(date_value)

total_months_count = len(total_months)
print("Total Months:", total_months_count)

# Calculate the net Profit/Loss
total_profit= 0
with open("budget_data.csv", mode='r') as file:
    csvreader = csv.DictReader(file)        
    
    for row in csvreader:
            try:
                profit_loss = int(row["Profit/Losses"])
                # Add the profit/loss value from the third column to the total
                total_profit += profit_loss #add to the total sum
            except ValueError:
                print(f"Skipping row with invalid dat: {row}")
print(f"Total : ${total_profit}")

changes = []

# Open the CSV file
with open('budget_data.csv', mode='r') as file:
    csvreader = csv.DictReader(file)
    
    # Check each row in the CSV file
    for row in csvreader:
        try:
            # Add the "Profit/Losses" numbers to the list as an integer
            profit_losses.append(int(row["Profit/Losses"]))
        except ValueError:
            print(f"Skipping row with invalid data: {row}")

# Calculate the changes between consecutive months
for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i - 1]
    changes.append(change)

# Calculate the average change
if changes:  # Check if there are any changes to avoid division by 0
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Print the results
print(f"Average Change in Profit/Losses: ${average_change:.2f}")


# Open the file with budget data
with open('budget_data.csv', mode='r') as file:
    csvreader = csv.DictReader(file)
    
    # Go over each row in the CSV file
    for row in csvreader:
        try:
            #Add date + "Profit/Losses" numbers to the lists
            dates.append(row["Date"])
            profit_losses.append(int(row["Profit/Losses"]))
        except ValueError:
            print(f"Skipping row with invalid data: {row}")

# Initialize variables to track the greatest increase
greatest_increase = 0
greatest_increase_date = ""

# Look at changes in value to find the greatest increase
for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i - 1]
    
    # Check if this is the greatest increase so far
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = dates[i]

# Print the results
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Date of Greatest Increase: {greatest_increase_date}")

#Calculate largest decrease

with open('budget_data.csv', mode='r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        try:
            #Add the date and "Profit/Losses" value to the lists
            dates.append(row["Date"])
            profit_losses.append(int(row["Profit/Losses"]))
        except ValueError:
            print(f"Skipping row with invalid data: {row}")

# Set variables to track the greatest decrease
        greatest_decrease = float('inf')  # Start with positive infinity
        greatest_decrease_date = ""

# Calculate changes and find the greatest decrease
    for i in range(1, len(profit_losses)):
        change = profit_losses[i] - profit_losses[i - 1]
    
    # Check if this is the greatest decrease so far
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = dates[i]

# Print the results
print(f"Greatest Decrease in Profits: ${greatest_decrease}")
print(f"Date of Greatest Decrease: {greatest_decrease_date}")

# Prepare results for output
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months_count}",
    f"Total: ${total_profit}",
    f"Average Change in Profit/Losses: ${average_change:.2f}",
    f"Greatest Increase in Profits: ${greatest_increase} on {greatest_increase_date}",
    f"Greatest Decrease in Profits: ${greatest_decrease} on {greatest_decrease_date}"
]

# Export results to a text file
with open('PyBank Analysis.txt', 'w') as file:
    for line in results:
        file.write(line + '\n')

print("Analysis results have been exported to 'financial_analysis.txt'")