# rps = rock-paper-cissors
import sys
import random
from enum import Enum

# Global variable
game_count = 0

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter ...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1, 2 or 3.")
        return play_rps()

    # Cast on int() the string
    player = int(playerchoice)
        
    # Random choice for player computer
    computerchoice = random.choice("123")

    computer = int(computerchoice)

    # Use Enum instead of print("You chose " + playerchoice + ".")
    # print("You chose " + str(RPS(player)) + ".") renvoie RPS.ROCK per example 
    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")
    # remplacer les print() par des \n

    # Nested function
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return("🎉 You win!")
        elif player == 2 and computer == 1:
            return("🎉 You win!")
        elif player == 3 and computer == 2:
            return("🎉 You win!")
        elif player == computer:
            return("😵 Tie game!")
        else : 
            return("🐍 Python wins!")
        
    game_result = decide_winner(player, computer)
    print(game_result)
    
    # Access to global variable outside the def play_rps()  
    # stock in global var so it is not clear at each play   
    global game_count
    game_count += 1
    
    print("\nGame count: " + str(game_count))

    print("\nPlay again?")
    
    while True:
        playagain = input("Y for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!")
        sys.exit("Bye! 👋\n")
   
# Call function rps
play_rps()
 
    
    

