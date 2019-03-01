# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:57:13 2019

@author: mikeg
"""

#import modules
import pandas as pd
import os
import csv 
df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyBoss\employee_data.csv', delimiter = ",")

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


#The SSN data should be re-written such that the first five numbers are hidden from view.


#The State data should be re-written as simple two-letter abbreviations.

