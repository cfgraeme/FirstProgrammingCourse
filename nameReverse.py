# nameReverse.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB4
# Due Date:     02.11.15
#
# Description: A program to reverse the name order for a file of names

infile = open("names.txt", "r")
for line in infile:
   x,y = str.split(line)
   y = y + ","
   print y, x

