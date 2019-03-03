# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:56:09 2019

@author: mikeg
"""

import re

line = ("Enter text or import file here.")

#Approximate word count
word_count = len(re.findall(r'\w+', line))
print ("The number of words in this paragraph: " + str(word_count) + ".")

#Approximate sentence count
sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', line.replace('\n',''))
sentences = sentences[:-1]
sentence_count = len(sentences)
print ("The number of sentences in this paragraph: " + str(sentence_count) + ".")

#Approximate letter count (per word)
words = line.split()
average = sum(len(word) for word in words) / len(words)
print ("The average number of letters in a word is: " + str(average) + ".")

#Average sentence length (in words)
avg = word_count/sentence_count
print ("The average number of words in a sentence is: " + str(avg) + ".")

