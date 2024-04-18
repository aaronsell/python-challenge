import os
import csv

' set the file path for the csv file '
csvpath = os.path.join("budget_data.csv")

' set the output path'
analysisText = os.path.join("financialAnalysis.txt")


totalProfitLosses = 0
totalMonths = 0
monthlyNetChange = []
numberMonths = []

' open the file for reading'
with open(csvpath) as budgetData:

    ' create the reader object'
    csvreader = csv.reader(budgetData) 

    'skips the header row'
    header = next(csvreader)

    ' initialize the row directly after the header'
    firstRow = next(csvreader)

    ' get the total number of months'
    totalMonths += 1

    ' gathers the total profits and losses'
    totalProfitLosses += float(firstRow[1])

    ' grab the first revenue in the number 1 index place'
    firstPrevious = float(firstRow[1])

    for row in csvreader:
        ' get the total number of months'
        totalMonths += 1

        ' gathers the total profits and losses'
        totalProfitLosses += float(row[1])

        ' track the monthly net change in revenue'
        totalChange = float(row[1]) - firstPrevious

        ' add the total change to the monthly change list'
        monthlyNetChange.append(totalChange)

        ' track the first change '
        numberMonths.append(row[0])

        ' update the profits and losses'
        firstPrevious = float(row[1])

' get the average change per month'
averageNetChange = (sum(monthlyNetChange) / len(monthlyNetChange))

greatestIncrease = [numberMonths[0], monthlyNetChange[0]]
greatestDecrease = [numberMonths[0], monthlyNetChange[0]]

' loop to find monthly greatest increase and decrease '
for indicator in range(len(monthlyNetChange)):

    ' get greatest increase'
    if (monthlyNetChange[indicator] > greatestIncrease[1]):

        ' store the value if its the new greater increase value'
        greatestIncrease[1] = monthlyNetChange[indicator]

        ' get the corresponding month of the greatest value'
        greatestIncrease[0] = numberMonths[indicator]

    if (monthlyNetChange[indicator] < greatestDecrease[1]):

        ' store the value if its the new greater decrease value'
        greatestDecrease[1] = monthlyNetChange[indicator]

        ' get the corresponding month of the greatest value'
        greatestDecrease[0] = numberMonths[indicator]


countRows = (f"\nFinancial Analysis \n"
    f"--------------------------- \n"
    f"Total Months: {totalMonths} \n"
    f"Total Profits/Losses: {totalProfitLosses:,.0f} \n"
    f"Average Change: {averageNetChange:,.2f} \n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} $({greatestIncrease[1]:,.0f}) \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} $({greatestDecrease[1]:,.0f})")

print(countRows)

with open(analysisText,"w") as textFile:
    textFile.write(countRows)