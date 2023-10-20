# rps = rock-paper-cissorsplayer_wins
import sys
import random
from enum import Enum

# Global variable replace with closure : def play_rps in def rps
# game_count = 0

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    # Nested function
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
        # Use f-strings
        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        # remplacer les print() par des \n

        # Nested function in nested function
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return("🎉 You win!")
            elif player == 2 and computer == 1:
                player_wins += 1
                return("🎉 You win!")
            elif player == 3 and computer == 2:
                player_wins += 1
                return("🎉 You win!")
            elif player == computer:
                return("😵 Tie game!")
            else : 
                python_wins += 1
                return("🐍 Python wins!")
            
        game_result = decide_winner(player, computer)
        print(game_result)
        
        # Access to global variable outside the def play_rps()  
        # stock in global var so it is not clear at each play   
        # global game_count replace with closure = nonlocal game_count
        nonlocal game_count
        game_count += 1
        
        # Add f-strings
        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

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
            
    # return the nested function        
    return play_rps


# Call function rps
# play = rps()
# Lauch the game
# play()

# Use module instead
rock_paper_scissors = rps()
# And launch rps only if LESSON14_rps_v7 is the main file
if __name__ == "__main__":
    rock_paper_scissors()

