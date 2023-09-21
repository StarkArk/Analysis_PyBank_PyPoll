# import libraries
import os
import csv
import sys

# Set the path to retrieve the budget data file for Pybank
pybank_csv = os.path.join("..", "Starter_Code", "Pybank", "Resources", "budget_data.csv")

# assign key metric for profit/loss and empty lists to hold the pybank data
total_profit_loss = 0
pybank_headers = []
pybank_months = []
pybank_profit_loss = []

# Open the file and create lists for the Pybank column data 
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    pybank_headers = next(csv_reader)

    # Fill lists for months and profit/loss
    for row in csv_reader:
        pybank_months.append(row[0])
        pybank_profit_loss.append(float(row[1]))
        

# Calculate Key Metrics
total_months = len(pybank_months)
total_amount_p_and_l = sum(pybank_profit_loss)

# Make a list of monthly profit/loss changes
pl_change = 0
max_pl_change = min(pybank_profit_loss)
min_pl_change = max(pybank_profit_loss)
pl_change_list = []

# Iterate month by month to find the profit and loss change while picking up the max/min values
for i in range(len(pybank_months)):
    if i == 0:
        pl_change_list.append(0)
    elif i > 0:
        pl_change = pybank_profit_loss[i] - pybank_profit_loss[i-1]
        pl_change_list.append(pl_change)

        if pl_change > max_pl_change:
            max_pl_change = pl_change
            max_pl_change_date = pybank_months[i]
        if pl_change < min_pl_change:
            min_pl_change = pl_change
            min_pl_change_date = pybank_months[i]

# The pl_change_list includes the first month value, which had no change,
# so the calc for the average does not include it
avg_pl_change = sum(pl_change_list[1:len(pl_change_list)])/(len(pl_change_list) - 1)

# Print results to Terminal
print("")
print("Financial Analysis")
print("")
print("--------------------------")
print("")
print(f"Total Months: {total_months}")
print("")
print(f"Total: ${round(total_amount_p_and_l)}")
print("")
print(f"Average Change: ${round(avg_pl_change, 2)}")
print("")
print(f"Greatest Increase in Profits: {max_pl_change_date} (${round(max_pl_change)})")
print("")
print(f"Greatest Decrease in Profits: {min_pl_change_date} (${round(min_pl_change)})")
print("")

# Write and export the results to a text file: pybank_financial_analysis.txt
# Found this sys module solution on stackoverflow:
# "https://stackoverflow.com/questions/23364096/how-to-write-output-of-terminal-to-file"
f = open("pybank_financial_analysis.txt", 'w')
sys.stdout = f

print("")
print("Financial Analysis")
print("")
print("--------------------------")
print("")
print(f"Total Months: {total_months}")
print("")
print(f"Total: ${round(total_amount_p_and_l)}")
print("")
print(f"Average Change: ${round(avg_pl_change, 2)}")
print("")
print(f"Greatest Increase in Profits: {max_pl_change_date} (${round(max_pl_change)})")
print("")
print(f"Greatest Decrease in Profits: {min_pl_change_date} (${round(min_pl_change)})")
print("")

f.close()