# Dependencies
import csv
import os

# Files to Load
file_to_load = "Bank/budget_data.csv"
file_to_output = "Bank/budget_analysis.txt"

# Variables to Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
great_date = ""
great_increase = 0
bad_date = ""
worst_decrease = 0

revenue_changes = []

# Read Files
with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        # print(row)

        # Keep track of changes
        revenue_change = int(row[1]) - prev_revenue
        # print(revenue_change)

        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row[1])
        # print(prev_revenue)

        # Determine the greatest increase
        if (int(row[1]) > great_increase):
            great_increase = int(row[1])
            great_date = row[0]

        if (int(row[1]) < worst_decrease):
            worst_decrease = int(row[1])
            bad_date = row[0]

        # Add to the revenue_changes list
        revenue_changes.append(int(row[1]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(great_date) + " ($" +  str(great_increase) + ")") 
    print("Greatest Decrease: " + str(bad_date) + " ($" +  str(worst_decrease) + ")")
    


# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(great_date) + " ($" + str(great_increase) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(bad_date) + " ($" + str(worst_decrease) + ")")