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
print(UniqueCands)

#The total number of votes each candidate won
candidatewin = df['Candidate'].value_counts()
Election_df = pd.DataFrame(candidatewin)

Election_df = Election_df.rename(
    columns={"Index": "Name", "Candidate": "Votes"})
Election_df.head()

#Change new candidatewin dataframe column name - FAIL
#candidatewin.rename({1: 'Candidate', 2: 'Votes'}, axis='columns')
#candidatewin['total'] = candidatewin.sum(axis=0)
Election_df['Percentage'] = (((df['Candidate'].value_counts())/TotalVotes)*100).round(2).astype(str) + '%'


#The winner of the election based on popular vote.
WinnerCand = Election_df.loc[Election_df['Percentage'].max(), 'Index']
print(WinnerCand)


#Summary of Election Data
