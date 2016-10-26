# packageShipper.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB08
# Due Date:     03.18.15
#
# Description: This program determines whether a package can be shipped, 
# as well as the cost of the package shipment.

from math import *

# get weight as input
x = input("Enter the weight of the package, in pounds: ")

# determine if weight is legal to ship - Part 1
def legalWeight():
   return x>0 and x<=100


# determine cost of shipment - Part 2
def packageCost():
   cost = 0
   if x > 0:
      cost = cost + 10
      if x > 2:
         cost = cost + ((ceil(x)-2)*3.75)
         if x > 70:
            cost = cost + 8
            return cost
         else:
            return cost
      else:
         return cost

# outputs whether package can be shipped and the cost - Part 3
if legalWeight() == False:
   print "This package is not a legal weight to be shipped."
else:
   print "The cost to ship this package is", packageCost()