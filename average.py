# average.py
# Student:    Marge Marshall
# email:      mmmarsha1@g.cofc.edu
# Assignment: LAB2
# Due Date:   1.28.15
#
#   A simple program to average two exam scores.  
#   Illustrates use of multiple input.

print "This program computes the average of three exam scores."
print

score1, score2, score3 = input("Enter three scores separated by commas: ")
average = (score1 + score2 + score3) / 3.0

print "The average of the scores is:", average
