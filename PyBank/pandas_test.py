import pandas as pd
import csv 
import sys
df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyBank\budget_data.csv', delimiter = ",")

df.columns

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
print('Total Months:')
print(BankCount)
print('Total:')
print(BankSum)
print('Average Change:')
print(BankAvg)
print('Greatest Increase in Profits:')
print(BankMax)
print('Greatest Decrease in Profits:') 
print(BankMin)
