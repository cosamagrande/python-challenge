# importing modules to read csv file from resources

import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

#creating lists
Monthbucket = []
Prf_loss = []
# Reading CSV file
with open (csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    Skipping Headers on file
    csv_header = next(csvreader)

# iterating over rows to count for # of months and Total Profit/loss
    for row in csvreader:
        Months = row[0]
        Monthbucket.append(Months)

        suma = row[1]
        Prf_loss.append(suma)

# printing results
print('Financial Analyses')
print('------------------')
print(f'Total Months: {len(Monthbucket)}')
print(f'Total: ${sum(map(int,Prf_loss))}')

























