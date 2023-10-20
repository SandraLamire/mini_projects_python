# Try all format in w3schools.com/python/ref_string_format.asp

person = "Sandra"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

# old methods
message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

# dictionary
player = { 'person': 'Sandra', 'coins': 3 }
# format(**name of dictonary)
message = "\n{person} has {coins} coins left.".format(**player)    
print(message)

# All methods print : Sandra has 3 coins left.


# f-strings method
print("\n******* f-strings *******")

message = f"\n{person} has {coins} coins left."
print(message)
# Sandra has 3 coins left.

message = f"\n{person} has {2 * 5} coins left."
print(message)
# Sandra has 10 coins left.

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)
# sandra has 10 coins left.

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)
# Sandra has 10 coins left.


# Formatting option
print("\n******* f-strings options *******")

num = 10
# .2f = 2 décimales fixes
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")
# 2.25 times 10 is 22.50

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
# 2.25 times 1 is 2.25
# 2.25 times 2 is 4.50
# 2.25 times 3 is 6.75
# 2.25 times 4 is 9.00
# 2.25 times 5 is 11.25
# 2.25 times 6 is 13.50
# 2.25 times 7 is 15.75
# 2.25 times 8 is 18.00
# 2.25 times 9 is 20.25
# 2.25 times 10 is 22.50

for num in range(1,11):
    # .2% multiply by 100 and add %
    print(f"{num} divided by 2.25 is {num / 4.52:.2%}")
# 1 divided by 2.25 is 22.12%
# 2 divided by 2.25 is 44.25%
# 3 divided by 2.25 is 66.37%
# 4 divided by 2.25 is 88.50%
# 5 divided by 2.25 is 110.62%
# 6 divided by 2.25 is 132.74%
# 7 divided by 2.25 is 154.87%
# 8 divided by 2.25 is 176.99%
# 9 divided by 2.25 is 199.12%
# 10 divided by 2.25 is 221.24%     

