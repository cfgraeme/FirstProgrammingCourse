# fibonacci.py
# Student:    Marge Marshall
# email:      mmmarsha1@g.cofc.edu
# Assignment: LAB09
# Due Date:   04.01.15
#
# Calculates the nth value in the fibonacci series, given the n
#

from math import *

#set accumulators and initial values
initial = 0
previous = 1
current = 1
fibonacci = 0

#get the n value for "nth number in series"
index = input("Input  an n to find the nth value in the fibonacci sequence: ")

# set fibonacci values for n = 1 and n = 2
if index > 0 and index <=2:
   fibonacci = 1
#advance the fibonacci sequence for any n larger than 2
while initial < index-2:
   initial = initial + 1
   fibonacci = current + previous
   previous = current
   current = fibonacci
   
#output final value
print fibonacci
