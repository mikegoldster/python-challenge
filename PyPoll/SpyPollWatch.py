# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:21:53 2019

@author: mikeg
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:11:11 2019

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

#The total number of votes each candidate won
df['percent'] = df['rent']/df['total']

candidatewin = df['Candidate'].value_counts()
candidatewin.columns = ['Candidate', 'Vote']
candidatewin['percentage'] = candidatewin.sum(axis=1)

#The percentage of votes each candidate won
candidatewin['Percentage'] = ((candidatewin['Vote'] / candidatewin['Vote'].sum())*100).round(2).astype(str) + '%'

#The winner of the election based on popular vote.
WinnerCand = candidatewin.loc[candidatewin['Vote'].idxmax()]
print(WinnerCand)

#Summary of Election Data
