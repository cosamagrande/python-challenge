# importing modules to read csv file from resources

import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

# Reading CSV file
with open (csvpath,'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    Skipping Headers on file
    csv_header = next(csvreader)

    #creating lists
    MonthList = []
    Prf_lossList = []

# iterating over rows to count for # of months and Total Profit/loss
    for row in csvreader:
        Months = row[0]
        MonthList.append(Months)

        suma = int(row[1])
        Prf_lossList.append(suma)

# printing results
print('Financial Analyses')
print('------------------')
print(f'Total Months: {len(MonthList)}')
print(f'Total: ${sum(map(int,Prf_lossList))}')

#Generating successive element difference within Prf_Loss list

Month_Diff = [Prf_lossList[i + 1] - Prf_lossList[i] for i in range(len(Prf_lossList)-1)] 

#Calculating average of Month_Diff

def Ave(Month_Diff):
    return sum(Month_Diff)/len(Month_Diff)
average = Ave(Month_Diff)

# printing results
print(f'Average Change: ${round(average,2)}')

# Finding min/max position/index in Month_Diff

minimum = Month_Diff.index(min(Month_Diff))
maximum = Month_Diff.index(max(Month_Diff))

# printing results
print(f'Greatest Increase in Profits: {MonthList[maximum +1]} (${max(Month_Diff)})')
print(f'Greatest Decrease in Profits: {MonthList[minimum +1]} (${min(Month_Diff)})')

















 






















