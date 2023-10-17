# String data type
print("String data type :".upper())
print()

# literal assignment
print("literal assignment".upper())
first = "Sandra"
last = "Lamiré"
print(type(first))
# <class 'str'>
print(type(first) == str)
# True
print(isinstance(first, str))
# True (est ce que first est une instance de string?)

# Constructor function
print("Constructor function".upper())
pizza = str("Pepperoni")
print(type(pizza))
# <class 'str'>
print(type(pizza) == str)
# True
print(isinstance(pizza, str))
# True
print()

# Concatenation
print("Concatenation".upper())
fullname = first + " " + last
print(fullname)
# Sandra Lamiré
fullname += "!"
print(fullname)
# Sandra Lamiré!
print()

# Casting a number to a string
print("Casting a number to a string".upper())
decade = str(1980)
print(decade)
# 1980
print(type(decade))
# <class 'str'>
statement = "I like rock music from the " + decade + "s."
print(statement)
# I like rock music from the 1980s.

# Multiple lines
print("Multiple lines".upper())
multiline = '''
Hey, how are you?

I was just checking in.
                            All good?
'''
print(multiline)
# Hey, how are you?
#
# I was just checking in.
#                             All good?

# Escaping special characters (\t = tab, \n = new line)
print("Escaping special characters".upper())
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)
# I'm back at work!       Hey!
# 
# Where's this at\located?
print()

# String methods
print("String methods".upper())
print(first)            # Sandra
print(first.lower())    # sandra
print(first.upper())    # SANDRA
print(first)            # Sandra

print(first.title())    # Sandra (1rst letter in uppercase, other in lowercase)
print(first.replace("dra", "drine"))    # Sandrine
print()

print(len(multiline))   # 82
multiline += "                              "
multiline = "                              " + multiline
print(len(multiline))   # 142


print(multiline.strip())
# Hey, how are you?
#
# I was just checking in.
#                             All good?
print(len(multiline))           # 142
print(len(multiline.strip()))   # 80
print(len(multiline.lstrip()))  # 111 (left justify)
print(len(multiline.rstrip()))  # 111 (right justify)
print()

# Build a menu
print("Build a menu :".upper())
title = "menu".upper()
print(title.center(20, "="))    # Total = 20 characters
# ========MENU========
# left justify + complete with points until 16 characters
print("Coffee".ljust(16, ".") + "$1".rjust(4))  
# Coffee..........  $1
print("Muffin".ljust(16, ".") + "$2".rjust(4)) 
print("Cheesecake".ljust(16, ".") + "$4".rjust(4)) 
# ========MENU========
# Coffee..........  $1
# Muffin..........  $2
# Cheesecake......  $4
print()

# string index values
print("String index values :".upper())
print(first[1])                 # a
print(first[-2])                # r
print(first[1:-2])              # and (last index exclude)
print(first[1:])                # andra
print()

# Some methods return boolean data
print("Some methods return boolean data :".upper())
print(first.startswith("S"))    # True
print(first.startswith("s"))    # False
print(first.endswith("z"))      # False
print()

# Boolean data type
print("Boolean data type :".upper())
myvalue = True
x = bool(False)
print(type(x))                  # <class 'bool'>
print(isinstance(myvalue, bool))# True
print()

# Numeric data types
print("Numeric data types :".upper())
print()

# integer type
print("integer type".upper())
price = 100
best_price = int(80)
print(type(price))                  # <class 'int'>
print(isinstance(best_price, int))  # True
print()

# float type
print("float type".upper())
gpa = 3.28
y = float(1.14)
print(type(gpa))                # <class 'float'>
print()

# complexe type
print("complexe type".upper())
comp_value = 5+3j
print(comp_value)               # (5+3j)
print(comp_value.real)          # 5.0
print(comp_value.imag)          # 3.0
print()

# Built-in functions for numbers
print("Built-in functions for numbers".upper())
print(abs(gpa))                 # 3.28
print(abs(gpa * -1))            # 3.28
print(round(gpa))               # 3
print(round(gpa, 1))            # 3.3
print()

print("Built-in functions with math import".upper())
import math                     # on the top of page
print(math.pi)                  # 3.141592653589793
print(math.sqrt(64))            # 8.0
print(math.ceil(gpa))           # 4
print(math.floor(gpa))          # 3     
print()

# Casting a string to number
print("Casting a string to number".upper())
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))          # <class 'int'>

# Error if you attempt to cats incorrect data
# zip_value = int("New York")
# ValueError: invalid literal for int() with base 10: 'New York'
print()




