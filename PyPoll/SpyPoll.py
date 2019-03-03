# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:11:11 2019

@author: mikeg
"""

#import modules
import pandas as pd
import numpy as np
import os
import csv 
df = pd.read_csv(r'C:\Users\mikeg\OneDrive\Desktop\RiceDataCamp\GitClone\python-challenge\PyPoll\election_data.csv', delimiter = ",")

#The total number of votes cast
TotalVotes = df['Voter ID'].count()

#A complete list of candidates who received votes
UniqueCands = df['Candidate'].unique()

#Total votes won by each candidate
candidate_counts = df['Candidate'].value_counts()

#The percentage of votes each candidate won
candidate_totals = pd.DataFrame({'Candidate': UniqueCands, 'Votes': candidate_counts})
candidate_totals['Votes'] = pd.to_numeric(candidate_totals['Votes'])
candidate_totals['Percentage'] = (((candidate_totals['Votes'])/TotalVotes)*100).round(2).astype(str) + '%'


#The winner of the election based on popular vote.
WinnerCand = candidate_totals['Votes'].max()
Winner = candidate_totals.loc[candidate_totals["Votes"] == WinnerCand]

#Set index to Candidate..
finalcand = candidate_totals.set_index("Candidate")

#The winner of the election based on popular vote.
WinnerCand = candidate_totals.loc[candidate_totals['Votes'].idxmax(), 'Candidate']

#Summary of Election Data
print("Election Results")
print("-------------------------")
print("Total Votes: ")
print(TotalVotes)
print("-------------------------")
print(finalcand)
print("-------------------------") 
print("Winner: ")
print(WinnerCand)
print("-------------------------")
