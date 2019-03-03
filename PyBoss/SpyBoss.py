# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:57:13 2019

@author: mikeg
"""

#import modules
import pandas as pd
import os
import csv 

#Import the employee_data1.csv and employee_data2.csv 

df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyBoss\employee_data.csv')

#The Name column should be split into separate First Name and Last Name columns.
# new data frame with split value columns 
new = df["Name"].str.split(" ", n = 1, expand = True) 
 
# making seperate first name column from new data frame 
df["First Name"]= new[0] 

# making seperate last name column from new data frame 
df["Last Name"]= new[1] 

# Dropping old Name columns 
df.drop(columns =["Name"], inplace = True) 

#The DOB data should be re-written into MM/DD/YYYY format.
df['DOB'] = pd.to_datetime(df['DOB']).dt.strftime('%m/%d/%Y')

#The SSN data should be re-written such that the first five numbers are hidden from view.
df['SSN'] = df['SSN'].str.replace(r'^\d{3}-\d{2}', "***-**", regex=True)

#The State data should be re-written as simple two-letter abbreviations.
us_state_abbrev = {
'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
df['State'] = df['State'].map(us_state_abbrev).fillna(df['State'])
