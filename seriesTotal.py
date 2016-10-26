# seriesTotal.py
#
# Student:     Marge Marshall
# email:       mmmarsha1@g.cofc.edu
# Assignment:  LAB2
# Due Date:    1.28.15
#
# A program to compute the average of a series of numbers entered by the user


print "This program will find the sum of a series of numbers."

numinSeries = input("How many numbers are you adding together? ")
total = 0.0
print "Enter the numbers from the series, one at a time."

for i in range(numinSeries):
    number = input("Enter a number from the series: ")
    total = total + number

print "The total of these", numinSeries, "numbers is: ", total
  
