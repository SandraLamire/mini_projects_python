# rps = rock-paper-cissors
import sys
import random
from enum import Enum

# Enum = values doesn't change
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# print(RPS(2)) renvoie RPS.PAPER
# print(RPS.ROCK) renvoie RPS.ROCK
# print(RPS['ROCK']) renvoie RPS.ROCK
# print(RPS.ROCK.value) renvoie 1
# sys.exit() for execute the code below only

print("")
playerchoice = input("Enter ...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

# Cast on int() the string
player = int(playerchoice)

if player < 1 or player > 3:
    # stop program
    sys.exit("You must enter 1, 2 or 3.")
    
# random choice for player computer
computerchoice = random.choice("123")

computer = int(computerchoice)

print()
# Use Enum instead of print("You chose " + playerchoice + ".")
# print("You chose " + str(RPS(player)) + ".") renvoie RPS.ROCK per example 
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print()

# Who win?
if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😵 Tie game!")
else : 
    print("🐍 Python wins!")

 

    
    
    

