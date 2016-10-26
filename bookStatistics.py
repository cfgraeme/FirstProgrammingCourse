# bookStatistics.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB4
# Due Date:     02.11.15
#
# Description: A program to find the total word count and average word
# length of a text document

infileName = raw_input("What file would you like to get some statistics on? ")
infile = open(infileName, 'r')

x = infile.read()

y = str.split(x)
total = 0.0
for i in y:
   total = total + len(i)
average = total/len(y)
print "The average word length is", average

print "The word count of this file is", len(str.split(x))

