# Closure is a function having access to the scope
# of its parent function (nested function)
# after the parent function has returned

# Use a variable of parent in child with keyword nonglobal

def parent_function(person, coins):
    # coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
    # parent function return child function
    return play_game


tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
# Tommy has 2 coins left.
tommy()
# Tommy has 1 coin left.
jenny()
# Jenny has 4 coins left.
tommy()
# Tommy is out of coins.

