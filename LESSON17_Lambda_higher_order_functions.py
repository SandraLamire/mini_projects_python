# LAMBA

# squared : lambda num : num * num
def squared(num): return num * num
print(squared(2))
# 4

# addTwo = lambda num : num + 2
def addTwo(num): return num + 2
print(addTwo(12))
# 14

# Lambda with parameters
# lambda a,b : a + b
def sum_total(a,b): return a + b
print(sum_total(10,8))
# 18

##############################################

# Function that we don't want to re use 
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))    # 17
print(addTwenty(7)) # 27

##############################################

# HIGHER ORDER FUNCTION

##############################################

# MAP

# Function with 1 or + functions in argument
# Or function that returns a function as a result
numbers = [3,7,12,18,20,21]

# map = function in first argument, list in second arg
# map avoid loop
squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))
# [9, 49, 144, 324, 400, 441]

##############################################

# FILTER

# Return True for odd numbers (= impaires, even = pairs)
# lambda num : num % 2 != 0

# Return the True results
odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))
# [3, 7, 21]

##############################################

# REDUCE (= ADD)

# Automatic import at the record if it'snt notify here
from functools import reduce

# Reduce = 2 parameters : accumulator (=subtotal), current item
# lambda acc, curr: acc + curr
numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)
# 16

# Equal to Reduce
print(sum(numbers))
# 16

# Reduce, like Sum can have a starting value
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)
print(sum(numbers, 10))
# 26

# lambda acc, curr : acc + len(curr)

names = ['Sandra', 'Dave', 'John Jingleheimerschmidt']

# Starting value not optional here
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
# 34



