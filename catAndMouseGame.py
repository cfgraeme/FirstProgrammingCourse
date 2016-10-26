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
# Points are accumulated by moving around the screen for both players.

from gui import *
from math import *

d1 = Display("Cat N Mouse", 800, 800)
d1.setColor(Color(255, 255, 255))

def catSpeed(x): #set speed of cat using a slider
   global increment
   increment = x
slider1 = Slider(HORIZONTAL, 1, 20, 3, catSpeed)

#set start message for game
beginText = Label("Use slider to determine cat speed (1-20), then press shift to start.", CENTER) 
beginText.setFont(Font( 'Monospaced', Font.PLAIN, 18))

d1.add(beginText, 30, 400)
d1.add(slider1, 280, 450)

# set variables for game
catX = 600
catY = 600
mouseX = 1
mouseY = 1
cheeseX = 700
cheeseY = 740

# establish icons
cat = Icon("cat.png") # cat size x: 96 y:132
mouse = Icon("mouse.png") # mouse size x:56 y:64
cheese = Icon("cheese.png") # cheese size x:100 y:57

#game outcomes
catWins = False  #set both outcomes to False initially (accumulator)
mouseWins = False
catScore = 0
mouseScore = 0
mouseWinString = "GAME OVER: MOUSE WINS! SCORE: "
mouseWinMessage = Label("                            ")
mouseWinMessage.setFont(Font( 'Monospaced', Font.PLAIN, 18))

catWinString = "GAME OVER: CAT WINS! SCORE: "
catWinMessage = Label("                            ")
catWinMessage.setFont(Font( 'Monospaced', Font.PLAIN, 18))

#functions for gameplay
def mouseRuns(x, y):  #moves mouse
   global mouseX, mouseY, catX, catY, cheeseX, cheeseY, catWins, mouseWins, mouseScore, catScore
   mouseX = x
   mouseY = y
   d1.move(mouse, mouseX, mouseY)
   if catWins == False and mouseWins == False: #accumulates score for mouse
      mouseScore = mouseScore + 1
      
   if catWins == False: #determines winner
      if ((mouseX >= cheeseX and mouseX <= cheeseX + 99) or (mouseX + 55 >= cheeseX and mouseX + 55 <= cheeseX + 99)) and ((mouseY >= cheeseY and mouseY <= cheeseY + 56) or (mouseY + 63 >= cheeseY and mouseY + 63 <= cheeseY + 56)):
         mouseWins = True
         mouseWinMessage.setText(mouseWinString + str(mouseScore)) #displays outcome and score when the mouse wins
         d1.add(mouseWinMessage, 200, 400)
         
   elif mouseWins == False:
      if ((mouseX >= catX and mouseX <= catX + 95) or (mouseX + 55 >= catX and mouseX + 55 <= catX + 95)) and ((mouseY >= catY and mouseY <= catY + 131) or (mouseY + 63 >= catY and mouseY + 63 <= catY + 131)):
         catWins = True
         catWinMessage.setText(catWinString + str(catScore)) #displays outcome and score when the cat wins
         d1.add(catWinMessage, 200, 400)

def keyPress(key): 
   global catX, catY, mouseX, mouseY, cheeseX, cheeseY, increment, catWins, mouseWins, mouseScore, catScore
   
   if key == VK_SHIFT:  #starts game
      d1.remove(beginText)
      d1.remove(slider1)
      d1.add(cat, catX, catY)
      d1.add(cheese, cheeseX, cheeseY)
      d1.add(mouse, mouseX, mouseY) 
       
   if key == VK_RIGHT:   #moves cat
     catX = catX + increment
     if catWins == False and mouseWins == False:
        catScore = catScore + increment #accumulate score for cat
   elif key == VK_LEFT:
     catX = catX - increment
     if catWins == False and mouseWins == False:
        catScore = catScore + increment
   if key == VK_DOWN:
     catY = catY + increment
     if catWins == False and mouseWins == False:
        catScore = catScore + increment
   elif key == VK_UP:
     catY = catY - increment
     if catWins == False and mouseWins == False:
        catScore = catScore + increment 
   d1.move(cat, catX, catY)

   if mouseWins == False: #determines winner
      if ((mouseX >= catX and mouseX <= catX + 95) or (mouseX + 55 >= catX and mouseX + 55 <= catX + 95)) and ((mouseY >= catY and mouseY <= catY + 131) or (mouseY + 63 >= catY and mouseY + 63 <= catY + 131)):
         catWins = True
         catWinMessage.setText(catWinString + str(catScore)) #displays outcome and score when the cat wins
         d1.add(catWinMessage, 200, 400)
   elif catWins == False:
      if ((mouseX >= cheeseX and mouseX <= cheeseX + 99) or (mouseX + 55 >= cheeseX and mouseX + 55 <= cheeseX + 99)) and ((mouseY >= cheeseY and mouseY <= cheeseY + 56) or (mouseY + 63 >= cheeseY and mouseY + 63 <= cheeseY + 56)):
         mouseWins = True
         mouseWinMessage.setText(mouseWinString + str(mouseScore)) #displays outcome and score when the mouse wins
         d1.add(mouseWinMessage, 200, 400)

  
d1.onKeyDown(keyPress)
d1.onMouseMove(mouseRuns) 

    
