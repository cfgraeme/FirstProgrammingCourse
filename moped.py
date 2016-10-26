## Moped.py

# Insert the function cost() at the position shown below.
# DO NOT change main.
# Marge Marshall

import math

def main():
    print("Type : 50 cc Mopette")
    print("Hours: 2.25 ")
    print("Day  : weekday")
    print "The cost of rental was $%0.2f" % cost(50, 2.25, "weekday")
    print
    print("Type : 50 cc Mopette")
    print("Hours: 5.5 ")
    print("Day  : weekend")
    print "The cost of rental was $%0.2f" % cost(50, 5.5, "weekend")
    print
    print("Type : 250 cc Mohawk")
    print("Hours: 4.5 ")
    print("Day  : weekday")
    print "The cost of rental was $%0.2f" % cost(250, 4.5, "weekday")
    print
    print("Type : 50 cc Mopette")
    print("Hours: 3 ")
    print("Day  : weekday")
    print "The cost of rental was $%0.2f" % cost(50, 3, "weekday")
    print
    print("Type : 250 cc Mohawk")
    print("Hours: 1.75 ")
    print("Day  : weekday")
    print "The cost of rental was $%0.2f" % cost(250, 1.75, "weekday")
    print
    print("Type : 250 cc Mohawk")
    print("Hours: 6 ")
    print("Day  : weekend")
    print "The cost of rental was $%0.2f" % cost(250, 6, "weekend")
    print

# Insert cost() here.
def cost(cc, hours, day):
   cost = 15
   if hours > int(hours): #round hours up if a fraction of an hour
       hours = int(hours) +1 
   if cc == 50:
      if day == "weekday":
         if hours >3.0:
            cost = cost + (hours - 3)*2.5
      if day == "weekend":
          cost = cost + 15
          if hours >3.0:
            cost = cost + (hours - 3)*7.5
   if cc == 250:
      cost = cost + 10
      if day == "weekday":
         if hours >3.0:
            cost = cost + (hours - 3)*3.5
      if day == "weekend":
         cost = cost + 10
         if hours >3.0:
            cost = cost + (hours - 3)*8.5

   return cost
main()
