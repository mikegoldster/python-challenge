# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:26:25 2019

@author: mikeg
"""

#import modules
import pandas as pd
import os
import csv 
df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyPoll\election_data.csv', delimiter = ",")

#The total number of votes cast
TotalVotes = df['Voter ID'].count()
print(TotalVotes)

#A complete list of candidates who received votes
UniqueCands = df['Candidate'].unique()
UniqueCands.head() 
