
import csv
import sys
import locale

# Path 
csvpath = '/Users/xavier/Documents/GitHub/python-challenge1/PyBank/Resources/budget_data.csv'

# Open and read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header line
    next(csvreader)

    # Fetch the first row for initial setup
    row = next(csvreader)
    month, amount = row
    amount = int(amount)

    # Initialize variables
    total = amount
    count = 0
    previous_amount = amount
    sum_delta = 0
    max_profit = 0
    min_profit = sys.maxsize

    # Loop through remaining rows
    for row in csvreader:
        month, amount = row
        amount = int(amount)
        count += 1
        total += amount

        delta = amount - previous_amount
        sum_delta += delta
        previous_amount = amount

        if delta > max_profit:
            max_profit = delta
            max_month = month

        if delta < min_profit:
            min_profit = delta
            min_month = month

    # Calculate average change and round it
    avg_delta = round(sum_delta / count, 2)

    # Format currency 
    locale.setlocale(locale.LC_ALL, '')
    total = locale.currency(total, grouping=True)
    avg_delta = locale.currency(avg_delta, grouping=True)
    max_profit = locale.currency(max_profit, grouping=True)
    min_profit = locale.currency(min_profit, grouping=True)

# Output 
with open('Budget_Data.txt', 'w') as file:
    print("Financial Analysis")
    file.write("Financial Analysis\n")

    print("-----------------------------")
    file.write("-----------------------------\n")

    print("Total Months:" + str(count))
    file.write("Total Months:" + str(count) + '\n')

    print("Total:" + str(total))
    file.write("Total:" + str(total) + '\n')

    print("Average Change:" + avg_delta)
    file.write("Average Change:" + avg_delta + '\n')

    print(f"Greatest Increase in Profit {max_month} ({max_profit})")
    file.write(f"Greatest Increase in Profit {max_month} ({max_profit})\n")

    print(f"Greatest Decrease in Profit {min_month} ({min_profit})")
    file.write(f"Greatest Decrease in Profit {min_month} ({min_profit})\n")
