# hiLoGame.py
# Student:    Marge Marshall
# email:      mmmarsha1@g.cofc.edu
# Assignment: LAB09
# Due Date:   04.01.15
#
# Gives the user 7 guesses to determine a pseudo-random number between 1 and 100.
#

from math import *
from random import randrange


truenum = randrange(1, 101)
guesscount = 1
guess = input("Guess the generated number, between 1 and 100: ")

while guesscount < 7 and guess != truenum:
   if guess > truenum:
      print "too high"
   elif guess < truenum:
      print "too low"
   guess = input("Guess the generated number, between 1 and 100: ")
   guesscount = guesscount + 1

if guess == truenum:
   print "correct!"
   print "You won in", guesscount, "guesses!"
else:
   print "Sorry, you lose, The number was "+str(truenum)+"."
   
