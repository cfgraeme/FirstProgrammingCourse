# palindrome.py
# Student:    Marge Marshall
# email:      mmmarsha1@g.cofc.edu
# Assignment: LAB09
# Due Date:   04.01.15
#
# A program to determine whether or not a string is a palindrome 
#

from string import *
from math import *

pal = raw_input("Input the string in all lowercase, with no spaces or punctuation: ")

length = len(pal)
mid = length/2
accum = 0
palindrome = True
#left side of palindrome starting from the middle
initL = pal[length/2 - 1 - accum]
#right side of palindrome starting from the middle, only for even
initRE = pal[length/2 + accum]
#right side of palindrome starting from the middle, only for odd
initRO = pal[length/2 + 1 + accum]

# for even
if length/2.0 == length/2:
   while accum < mid:
      accum = accum + 1
      if initRE != initL:     
         palindrome = False

# for odd   
elif length/2.0 > length/2 :
   while accum < mid:
      accum = accum + 1
      if initRO != initL:     
         palindrome = False


if palindrome:
   print "Input is a palindrome."
else:
   print "Input is not a palindrome."
