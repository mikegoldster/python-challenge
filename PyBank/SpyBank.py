import pandas as pd
import os
import csv 
df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyBank\budget_data.csv', delimiter = ",")

# The total number of months included in the dataset
BankCount = df['Date'].count()
# The net total amount of "Profit/Losses" over the entire period
BankSum = '${:.0f}'.format(df['Profit/Losses'].sum())


#Determine the amount of increase or decrease from the previous month
AmtChange = df["Profit/Losses"].diff()
df["Amount Changed"] = AmtChange

# The greatest increase in profits (date and amount) over the entire period
BankMax = df.loc[df['Profit/Losses'].idxmax(), 'Date']
GreatestIncrease = '${:.0f}'.format(df["Amount Changed"].max())

# The greatest decrease in losses (date and amount) over the entire period
BankMin = df.loc[df['Profit/Losses'].idxmin(), 'Date']
GreatestDecrease = '${:.0f}'.format(df["Amount Changed"].min())

# The average of the changes in "Profit/Losses" over the entire 
BankAvg = '${:.2f}'.format(df["Amount Changed"].mean())

print('Total Months:')
print(BankCount)
print('Total:')
print(BankSum)
print('Average Change:')
print(BankAvg)
print('Greatest Increase in Profits:')
print(BankMax)
print(GreatestIncrease)
print('Greatest Decrease in Profits:') 
print(BankMin)
print(GreatestDecrease)
