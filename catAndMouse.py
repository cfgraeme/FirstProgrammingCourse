# catAndMouse.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220L, Section 02
# Assignment:   LAB06
# Due Date:     02.25.15
#
# Description: This program moves the mouse around the cat by way of the cursor.

from gui import *

d1 = Display("Cat N Mouse", 400, 400)
d1.setColor(Color(240, 230, 255))

cat = Icon("cat.png")  #adds icons to the display
mouse = Icon("mouse.png")
d1.add(cat, 200, 200)
d1.add(mouse)

def mouseRuns(x, y):  #moves mouse around display according to x, y coordinates
   d1.move(mouse, x, y)
   
d1.onMouseMove(mouseRuns) #sets x, y coordinates according to mouse coordinates