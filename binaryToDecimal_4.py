# binaryToDecimal_4.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB3
# Due Date:     02.04.15
#
# This program converts binary numbers to base-ten numbers.

total = 0
power = 1
n = raw_input("Enter a number in binary, i.e. a string of 0s and 1s: ")
for i in n:
   total = total + (int(i)*(2**(len(n) - power)))
   power = power+1
print int(n), "(binary) equals", total, "(decimal)"
   

