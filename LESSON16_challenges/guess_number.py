# guess_number.py

import sys
import random
import os

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal game_count
        
        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please guess 1, 2, or 3.\n")
            return play_guess_number()
        
        computerchoice = int(random.choice("123"))

        print(f"\n{name}, you chose {playerchoice}")
        print(f"I was thinking about the number {computerchoice}.\n")
        
        player = int(playerchoice)
        computer = int(computerchoice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!\n"
            else:
                return f"Sorry, {name}. Better luck next time...😢\n"

        game_result = decide_winner(player, computer)
        print(game_result)
        
        game_count += 1
        print(f"Game count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        
        print(f"Your winning percentage: {player_wins / game_count * 100:.2f}%")
        
        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("Y for Yes or Q to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else: 
                break
            
        if playagain.lower() == 'y':
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing Guess the number!")
            # Si le jeu est lancé seul
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            # si le jeu est lancé depuis Arcade
            else : 
                return
    return play_guess_number        
            
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
    description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
