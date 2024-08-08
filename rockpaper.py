# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

c = random.randint(1,3)

player = int (input("Enter 1 for ROCK, Enter 2 for PAPER , Enter 3 for SCISSORS"))
#if (player>3 or player<1):
 #   print("invalid input")

if (c == player ):
       print (c,"Match Draw")
elif (c == 1 and player == 2):
        print (c,"You Win ")
elif (c == 1 and player == 3):
        print(c,"Computer Wins")
elif (c == 2 and player == 1):
        print(c,"Computer Wins ")
elif (c== 2 and player == 3):
        print(c,"You win")
elif (c == 3 and player == 2):
        print(c,"Computer Wins ")
else:
      print(c,"You win")
