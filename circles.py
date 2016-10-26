# circles.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB7
# Due Date:     03.11.15
#
# This program determines whether or not two circles intersect, given inputs
#

from gui import *
from math import *

d = Display("Circles", 400, 400)

print "This program finds out whether 2 circles intersect, given their xy coordinates and the radii."

# Get parameters for the circles
x1, y1 = input("Enter the x and y coordinates of the first circle, separated by a comma: ")
r1 = input("Enter the radius of the first circle: ")
x2, y2 = input("Enter the x and y coordinates of the second circle, separated by a comma: ")
r2 = input("Enter the radius of the second circle: ")

circle1 = Circle(x1, y1, r1)
circle2 = Circle(x2, y2, r2)

d.add(circle1)
d.add(circle2)

#Find the distance between the center of the two circles
eucl = sqrt(((x2-x1)**2)+((y2-y1)**2))

if eucl >= r1 + r2:
   print "These circles do not intersect."
else:
   print "These circles intersect."
