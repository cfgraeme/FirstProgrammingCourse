# fahrenheitToCelsius.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220
# Assignment:   Homework #1
# Due Date:     1.30.15
#
# Purpose: This program converts degrees Fahrenheit to degrees Celsius.
#
# Input:     The degrees in Fahrenheit.  No error checking is performed 
#               (i.e., we assume the user makes no mistake when entering these values).
#
# Output:  The corresponding degrees in Celsius. 

print "This program will convert temperature from Fahrenheit degrees to Celsius."

fahrenheit = input("Enter the temperature, in fahrenheit: ")
celsius = (fahrenheit - 32.0)*5.0/9.0

print "The temperature is", round(celsius, 2), "degrees celsius."
