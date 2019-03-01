import csv
import sys
import pandas as pd

with open('budget_data.csv') as f:
   reader = csv.DictReader(f)
   line_count = 0
   for row in reader:
    line_count += 1
    print(f'Total months: {line_count}.')


total = sum(int(r[1]) for r in csv.DictReader(f)
print(f'Total: {total}.')

df = pd.dataframe(f)
print(df)

# The total number of months included in the dataset
BankCount = df['Date'].count()
# The net total amount of "Profit/Losses" over the entire period
BankSum = df['Profit/Losses'].sum()
# The average of the changes in "Profit/Losses" over the entire 
BankAvg = df['Profit/Losses'].mean()
# The greatest increase in profits (date and amount) over the entire period
BankMax = df['Profit/Losses'].max()
# The greatest decrease in losses (date and amount) over the entire period
BankMin = df['Profit/Losses'].min()

#Display the results.
print('Total Months: {BankCount}.')
print('Total: {BankSum}.')
print('Average Change: {BankAvg}.')
print('Greatest Increase in Profits: {BankMax}.')
print('Greatest Decrease in Profits: {BankMin}.')