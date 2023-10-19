value = 1

# while value < 10:
#     print(value)
#     value += 1
# # print 1 à 9

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
# # print 1 à 5

# while value <= 10:
#     print(value)
#     if value == 5:
#         continue
#     value += 1
# # loop infini car continue empêche le passage par l'incrémentation

# # incrémentation avant le continue sinon boucle infinie
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# # print 2 à 11 car print après l'incrémentation

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))
#     # cast en string pour eviter un typeError
# # print 2 à 11 puis Value is now equal to 11

names = ["Dave", "Sandra", "John"]
for x in names:
    print(x)
# Dave
# Sandra
# John

for x in "Mississippi":
    print(x)
# print M i s s i s s i p p i en vertical

for x in names:
    if x == "Sandra":
        break
    print(x)
# Dave

for x in names:
    if x == "Sandra":
        continue
    print(x)
# Dave John (car continue passe à l'itération suivante sans print Sandra)

# De 0 jusqu'à 3
for x in range(4):
    print(x)
# 0 1 2 3 en vertical

# De 2 jusqu'à 4
for x in range(2,4):
    print(x)
# 2 3 en vertical

# De 0 jusqu'à 100 azvec un pas de 5
for x in range(2,100,5):
    print(x)
else:
    print("Glad, that\'s over!")
# de 0 à 95 mais de 5 en 5 en vertical puis Glad that's over!

names = ["Dave", "Sandra", "John"]
actions = ["eats", "codes", "sleeps"]
for name in names:
    for action in actions:
        print(name + " " + action + ".")
# # Dave eats.
# # Dave codes.
# # Dave sleeps.
# # Sandra eats.
# # Sandra codes.
# # Sandra sleeps.
# # John eats.
# # John codes.
# # John sleeps.

for action in actions:
    for name in names:
        print(name + " " + action + ".")
# Dave eats.
# Sandra eats.
# John eats.
# Dave codes.
# Sandra codes.
# John codes.
# Dave sleeps.
# Sandra sleeps.
# John sleeps.



    



