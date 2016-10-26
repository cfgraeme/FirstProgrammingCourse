# catAndMouseGame.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220
# Assignment:   Homework #3
# Due Date:     03.23.15
#
# Description: This program is a game of cat and mouse.
# The mouse, moved by the mouse, must try to get the cheese.
# The cat, moved by the arrow keys, must keep the cheese safe, and try to catch the mouse.
# The game is over when the cat or mouse wins.

from gui import *
from math import *

d1 = Display("Cat N Mouse", 800, 800)
d1.setColor(Color(255, 255, 255))

def catSpeed(x): #set speed of cat using a slider
   global increment
   increment = x
slider1 = Slider(HORIZONTAL, 1, 20, 3, catSpeed)

beginText = Label("Use slider to determine cat speed (1-20), then press shift to start.", CENTER) #set start message for game
beginText.setFont(Font( 'Monospaced', Font.PLAIN, 18))

d1.add(beginText, 30, 400)
d1.add(slider1, 280, 450)

global catX, catY, mouseX, mouseY, cheeseX, cheeseY # set variables for game
catX = 600
catY = 600
mouseX = 1
mouseY = 1
cheeseX = 700
cheeseY = 740

global cat, mouse, cheese # establish icons
cat = Icon("cat.png") # cat size x: 96 y:132
mouse = Icon("mouse.png") # mouse size x:56 y:64
cheese = Icon("cheese.png") # cheese size x:100 y:57

global catWins, mouseWins # game outcomes
catWins = False  #set both outcomes to False initially (accumulator)
mouseWins = False

mouseWinMessage = Label("GAME OVER: MOUSE WINS")
mouseWinMessage.setFont(Font( 'Monospaced', Font.PLAIN, 18))

catWinMessage = Label("GAME OVER: CAT WINS")
catWinMessage.setFont(Font( 'Monospaced', Font.PLAIN, 18))

#functions for gameplay
def mouseRuns(x, y):  #moves mouse
   global mouseX, mouseY, catX, catY, cheeseX, cheeseY, catWins, mouseWins
   
   mouseX = x
   mouseY = y
   d1.move(mouse, mouseX, mouseY)

   
   if catWins == False: #determines winner
      if ((mouseX >= cheeseX and mouseX <= cheeseX + 99) or (mouseX + 55 >= cheeseX and mouseX + 55 <= cheeseX + 99)) and ((mouseY >= cheeseY and mouseY <= cheeseY + 56) or (mouseY + 63 >= cheeseY and mouseY + 63 <= cheeseY + 56)):
         d1.add(mouseWinMessage, 280, 400)
         mouseWins = True
   elif mouseWins == False:
      if ((mouseX >= catX and mouseX <= catX + 95) or (mouseX + 55 >= catX and mouseX + 55 <= catX + 95)) and ((mouseY >= catY and mouseY <= catY + 131) or (mouseY + 63 >= catY and mouseY + 63 <= catY + 131)):
         d1.add(catWinMessage, 280, 400)
         catWins = True

def keyPress(key): 
   global cat, mouse, cheese, catX, catY, mouseX, mouseY, cheeseX, cheeseY, increment, catWins, mouseWins
   
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

   if mouseWins == False:
      if ((mouseX >= catX and mouseX <= catX + 95) or (mouseX + 55 >= catX and mouseX + 55 <= catX + 95)) and ((mouseY >= catY and mouseY <= catY + 131) or (mouseY + 63 >= catY and mouseY + 63 <= catY + 131)):
         d1.add(catWinMessage, 280, 400)
         catWins = True
   elif catWins == False: #determines winner
      if ((mouseX >= cheeseX and mouseX <= cheeseX + 99) or (mouseX + 55 >= cheeseX and mouseX + 55 <= cheeseX + 99)) and ((mouseY >= cheeseY and mouseY <= cheeseY + 56) or (mouseY + 63 >= cheeseY and mouseY + 63 <= cheeseY + 56)):
         d1.add(mouseWinMessage, 280, 400)
         mouseWins = True
  
d1.onKeyDown(keyPress)
   
d1.onMouseMove(mouseRuns) 

    