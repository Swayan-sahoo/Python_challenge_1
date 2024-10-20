# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

#Dependencies
import csv
import os

#Files to load and output (update with correct file paths)
input_file = os.path.join("Resources", "budget_data.csv")  # Input file path
output_file = os.path.join("analysis", "budget_analysis.txt")  # Output file path

#Define variables to track the financial data
month_count = 0
total_sum = 0
months= []
monthly_changes=[]

#Add more variables to track other necessary financial data
highest_rise={"month": "","change":0}
#highest_rise ={"month": "","change": -float('inf')}
highest_fall ={"month": "","change": float("inf")}

#open and read the csv
with open(input_file) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    first_row = next(reader)
    month_count +=1
    total_sum += int(first_row[1])
    previous_value = int(first_row[1])

#Process each row of data
    for row in reader:
        month_count += 1
        current_value =int(row[1])
#Track the total
        total_sum +=current_value

#Track the net change
        monthly_change = current_value - previous_value
        previous_value = current_value

        months.append(row[0])
        monthly_changes.append(monthly_change)

#calculate the greatest increase in profits (month and amount)
        if monthly_change > highest_rise["change"]:
            highest_rise["month"] = row[0]
            highest_rise["change"] = monthly_change

#calculate the greatest decrease in losses (month and amount)
        if monthly_change < highest_fall["change"]:
            highest_fall["month"] = row[0]
            highest_fall["change"] = monthly_change


#calculate the average net change across the months
average_change = sum(monthly_changes) /len(monthly_changes)

#generate the output summary
output = (
    f"Budget Analysis Output\n"
    f"-----------------------\n"
    f"Total Count of Months: {month_count}\n"
    f"Total Sum of changes: ${total_sum}\n"
    f"Average change: ${average_change:2f}\n"
    f"Highest Increase in profits: {highest_rise['month']} (${highest_rise['change']})\n"
    f"Greatest Decrease in profits: {highest_fall['month']} (${highest_fall['change']})\n"

)

#print the output
print(output)



# Write the results to a text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
