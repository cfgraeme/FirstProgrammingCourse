# seriesAverage.py
#
# Student:     Marge Marshall
# email:       mmmarsha1@g.cofc.edu
# Assignment:  LAB2
# Due Date:    1.28.15
#
# A program to compute the average of a series of numbers entered by the user


print "This program will find the average of a series of numbers."

div = input("How many numbers are you averaging together? ")
total = 0.0
while div<0:
    div = input("Invalid number. please input a positive count value: ")
else:
   print "Enter the numbers from the series, one at a time."

   for i in range(div):
     number = input("Enter a number from the series: ")
     total = total + number

   average = total/div

   print "The average of these", div, "numbers is: ", average
  
