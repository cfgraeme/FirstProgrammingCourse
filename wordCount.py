# wordCount.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB4
# Due Date:     02.11.15
#
# Description: A program that counts the number of words in a sentence

x = raw_input("Enter the sentence you would like the word count of: ")
print "The word count of this sentence is", len(str.split(x))
