# ticTacToe.py
#
# Author:       Marge Marshall
# Email:        mmmarsha1@g.cofc.edu
# Class:        CSCI 220, Section 02
# Assignment:   HW4
# Due Date:     04.13.15
#
# Description: A game of tic tac toe played with a (dumb) computer.

"""this section contains functions that concern game setup; the possible spaces for moves and the format of the board."""

#creates necessary parameters for gameplay; the spaces on the board
def createBoard():
   board = [" "," "," "," "," "," "," "," "," ",]
   return board

#outputs the board in the correct tic tac toe format
def outputBoard(x):
   finalboard = " \n    |   |   \n  "\
                + x[0] + " | " + x[1] + " | " + x[2] +\
                " \n ---+---+---\n  "\
                + x[3] + " | " + x[4] + " | " + x[5] +\
                " \n ---+---+---\n  "\
                + x[6] + " | " + x[7] + " | " + x[8] +\
                " \n    |   |   \n"
   print finalboard

"""this section contains functions to determine if a board is full, whether there is a winner, and who the winner is."""

#determines if board is full
def isFull(x):
   boardFull = True
   for i in x:
      if i == " ":
         boardFull = False
   return boardFull     


#determines if there is a winner or not
def isWin(x):
   win = False
   if x[0]==x[1]==x[2]!=" " or\
      x[0]==x[3]==x[6]!=" " or\
      x[0]==x[4]==x[8]!=" " or\
      x[1]==x[4]==x[7]!=" " or\
      x[2]==x[4]==x[6]!=" " or\
      x[2]==x[5]==x[8]!=" " or\
      x[3]==x[4]==x[5]!=" " or\
      x[6]==x[7]==x[8]!=" ":
      win = True
   return win

#determines who has won the game, X or O (human or computer)
def whoIsWinner(x):
   winner = "none"
   if x[0]==x[1]==x[2]!=" ":
      winner = x[0]
   if x[0]==x[3]==x[6]!=" ":
      winner = x[0]
   if x[0]==x[4]==x[8]!=" ":
      winner = x[0]
   if x[1]==x[4]==x[7]!=" ":
      winner = x[1]
   if x[2]==x[4]==x[6]!=" ":
      winner = x[2]
   if x[2]==x[5]==x[8]!=" ":
      winner = x[2]
   if x[3]==x[4]==x[5]!=" ":
      winner = x[3]
   if x[6]==x[7]==x[8]!=" ":
      winner = x[6]
   return winner

#determines whether or not someone has won or if the board is full
def isGameOver(x):
   return isWin(x) or isFull(x)

"""this section contains functions that go through the mechanisms of gameplay; getting moves from human and computer, and updating the spaces on the board."""

#gets the input for the human move
def getHumanMove():
   move = input(" What square would you like to occupy? Pick 1-9: ")
   while move > 9 or move < 1 : #checks that entry is valid 
      move = input(" Invalid entry! Please pick a square 1-9: ")
   fmove = int(move) - 1
   return fmove

#gets number for the computer move
def getComputerMove(x):
   y = x + 1
   return y
   
#updates the board with human and computer moves
def updateBoard(x):
   newBoard = x
   humanMove = getHumanMove()
   while newBoard[humanMove] != " ": #doesn't allow double assignment or reassignment of a square
      print "already occupied"
      humanMove = getHumanMove()  
   newBoard[humanMove] = "X"
   computerMove = getComputerMove(-1)
   if not isGameOver(newBoard): #checks that a human win has not occurred before assigning a computer move to the board
      while newBoard[computerMove] != " ":  #doesn't allow double assignment or reassignment of a square
         computerMove = getComputerMove(computerMove)
      newBoard[computerMove] = "O"
   return newBoard

"""calls other functions to simulate the game of tic tac toe """

#play the game
def main():
   board = createBoard()
   outputBoard(board) #outputs blank board first
   while not isGameOver(board): #continues game while there is no draw and no winner
      nextBoard = updateBoard(board)
      board = nextBoard
      outputBoard(board)
   if isWin(board): #outputs winner/loser message
      if whoIsWinner(board) == "O":
         print " :( :( :( :( :( :( \n u lost 2 a computer \n that wasn't even tryin \n but just remeber bb \n i still believe in u. "
      if whoIsWinner(board) == "X":
         print "  :')  :')  :')  :') \n omg bb u !!~*~WoN~*~!! \n im so proud of u rn \n >~*^*~.~*^*~.~^*~<\n",\
               "    ____   ___     ___    ___ \n",\
               "   / __/  / _ \   / _ \  |   \ \n",\
               "  / / _  / / \ \ / / \ \ | |\ \ \n",\
               " / /_| | \ \_/ / \ \_/ / | |/ / \n",\
               " \_____|  \___/   \___/  |___/ \n",\
               "        _    ___    ____ \n",\
               "       | |  / _ \  |  _ \ \n",\
               "     _ | | / / \ \ | |/_/ \n",\
               "    \ \| | \ \_/ / | |\ \ \n",\
               "     \___|  \___/  |____/ \n",\

   else: #outputs draw message
      print " u dint win this game \n but u also dint lose \n so try2 stay posi bb \n ur still a gr8 playr \n :) :) :) :) :) :) :)"
      
main()
      
