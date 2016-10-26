# sphereFunctions.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB08
# Due Date:     03.18.15
#
# Description: This program calculates the area and volume of a sphere, given the radius.

from math import *

# get radius as input
radius = input("Enter the radius of the sphere: ")

# calculate sphere area
def sphereArea():
   area = 4*pi*(radius**2)
   return area
   
# calculate sphere volume
def sphereVolume():
   volume = (4/3)*pi*(radius**3)
   return volume
