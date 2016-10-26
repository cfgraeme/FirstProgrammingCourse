from gui import *

class Message(Display, Label):
   global d
   d = Display("", 400, 200)
   def __init__(self, message, color):
      self.message = message
      self.color = color
      global l
      l = Label(self.message, LEFT, color)
      d.add(l, 200, 100)
      
   def setMessage(self, message):
      self.message = message
      global l
      l.setText(self.message)
      d.add(l, 200, 100)
   
   def getMessage(self):
      return self.message
   
   def clear(self):
      self.message = ""
      global l
      l.setText(self.message)
      d.add(l, 200, 100)


   def setColor(self, color):
      self.color = color
      global l
      l.setForegroundColor(color)

   def getColor(self):
      return str(self.color)
  