# function name in lowercase + _ if necessary
def hello_world():
    print("Hello World!")
    
# Call the function
hello_world()
# Hello World!

def sum(num1, num2):
    print(num1 + num2)

# Call the function with arguments (not parameters)
sum(2,3)
# 5

# Return function
def sum2(num1, num2):
    return num1 + num2
total = sum2(2, 4)
print(total)
# 6

def sum3(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return 
    return num1 + num2
total = sum3("a", 4)
print(total)
# None

# total2 = sum3()
# print(total2)
# # TypeError: sum3() missing 2 required positional arguments: 'num1' and 'num2'

# total2 = sum3(1)
# print(total2)
# # TypeError: sum3() missing 1 required positional argument: 'num2'

# Default values
def sum3(num1=0, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return 
    return num1 + num2

total = sum3(1)
print(total)
# 4 (default value of num1=0)

def sum4(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2
total = sum4()
print(total)
# 0

# functions with numbers of arguments unknown = Tuples
def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items("Dave", "Sandra", "John") 
# ('Dave', 'Sandra', 'John')
# <class 'tuple'>

# Key worlds arguments = dictionary
def mult_names_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_names_items(first = "Dave", last = "Gigi") 
# {'first': 'Dave', 'last': 'Gigi'}
# <class 'dict'>








