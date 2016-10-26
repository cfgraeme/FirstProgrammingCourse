# wc.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220
# Assignment:   Homework 2
# Due Date:     02.20.15
#
# Description: A program to find the total word count, character count, and
# line count of a text document.

infileName = raw_input("What file would you like to get some statistics on? ")

infile = open(infileName, 'r')
y = infile.readlines()
total = 0  #initialize the line count
for line in y:
   total = total + 1

infile2 = open(infileName, 'r')
x = infile2.read()

print  total, len(str.split(x)), len(str(x))

