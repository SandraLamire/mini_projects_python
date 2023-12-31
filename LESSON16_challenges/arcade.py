# LAUNCH WITH : py .\LESSON16_challenges\arcade.py -n "Sandra"

import sys
from rps_v8 import rps
from guess_number import guess_number


def play_game(name='PlayerOne'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            line01 = "***************************************"  # Header
            line02 = "*                                     *"  # Re use
            line03 = f"*    Welcome back to the Arcade! 🕹️    *"  # Footer
            print()
            print(f"\t\tHello {name},\n")
            print(line01)
            print(line02)
            print(line03)
            print(line02)
            print(line01)
            
        playerchoice = input(
            "\nPlease, choose a game:\n1 = Guess the Number\n2 = Rock, Paper, Scissors\nOr press x to exit the Arcade\n"
        )
        
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.\n")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == '1':
            guess_my_number = guess_number(name)
            guess_my_number()
            # return

        elif playerchoice == '2':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
            # return
        else:
            print("\nSee you next time.")
            sys.exit(f"Goodbye {name}! 👋\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Arcade with game selection.")
    parser.add_argument("-n", "--name", metavar="name", required=True, help="The name of the player.")

    args = parser.parse_args()
    
    line01 = "***************************************"  # Header
    line02 = "*                                     *"  # Re use
    line04 = f"*       welcome to the Arcade! 🕹️      *"  # Footer
    print()
    print(f"\t\tHello {args.name},\n")
    print(line01)
    print(line02)
    print(line04)
    print(line02)
    print(line01)

    play_game(args.name)
    
