# findMax.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB7
# Due Date:     03.11.15
#
# This program finds the maximum value of 3 numbers using if else statements
#

print "This program finds the largest of 3 numbers."

a, b, c = input("Enter the three numbers, separated by commas: ")

if a>=b and a>=c:
   print "The greatest value is", a
elif b>=a and b>=c:
   print "The greatest value is", b
elif c>=b and c>=a:
   print "The greatest value is", c