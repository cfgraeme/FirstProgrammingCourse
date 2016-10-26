
from gui import *
from math import *

d1 = Display("Cat N Mouse", 400, 400)
d1.setColor(Color(255, 255, 255))

def catSpeed(x): #set speed of cat using a slider
   global increment
   increment = x


beginText = Label("Use slider to determine cat speed, then press shift to start.", CENTER) #set start message for game
beginText.setFont(Font( 'Monospaced', Font.PLAIN, 18))

# set variables for game
slider1 = Slider(HORIZONTAL, 0, 15, 3, catSpeed) 

d1.add(beginText, 55, 400)
d1.add(slider1, 280, 450)

# establish icons
global cat
cat = Icon("cat.png") # cat size x: 96 y:132
global mouse
mouse = Icon("mouse.png") # mouse size x:56 y:64
global cheese 
cheese = Icon("cheese.png") # cheese size x:100 y:57

# set variables for icon positions in x, y coordinates

global catX 
catX = 300
global catY 
catY = 300
global mouseX
mouseX = 1
global mouseY
mouseY = 1
global cheeseX
cheeseX = 300
global cheeseY
cheeseY = 340


#functions for gameplay

def mouseRuns(x, y):  #moves mouse
   global mouseX
   global mouseY
   mouseX = x
   mouseY = y
   d1.move(mouse, mouseX, mouseY)


def keyPress(key): #identifies actions that are caused by keyboard
   global cat, mouse, cheese, catX, catY, mouseX, mouseY, cheeseX, cheeseY, increment
   if key == VK_SHIFT:  #starts game
      d1.remove(beginText)
      d1.remove(slider1)
      d1.add(cat, catX, catY)
      d1.add(cheese, cheeseX, cheeseY)
      d1.add(mouse, mouseX, mouseY)  
   if key == VK_RIGHT:   #moves cat
     catX = catX + increment
   elif key == VK_LEFT:
     catX = catX - increment
   if key == VK_DOWN:
     catY = catY + increment
   elif key == VK_UP:
     catY = catY - increment
   d1.move(cat, catX, catY)

if cat.intersects(mouse) == True:
   print "here"