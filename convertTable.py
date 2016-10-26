# convertTable.py
#
# Student:    Marge Marshall
# Email:      mmmarsha1@g.cofc.edu
# Assignment: LAB2
# Due Date:   1.28.15
#
# This program shows temperatures in degrees celsius converted to degrees fahrenheit.

print "This program shows temperatures in degrees celsius converted to degrees fahrenheit."
print "Celsius|Fahrenheit"

for i in range(0, 101, 10):
   celsius = i
   fahrenheit = (9.0 / 5.0) * i + 32
   
   print celsius,"\t",  fahrenheit
