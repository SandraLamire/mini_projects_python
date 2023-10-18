users = ["Sandra", "Dave", "John"]

data = ["Sandra", 45, True]

emptylist = []

print("Sandra" in users)
# True
print("Sandra" in emptylist)
# False

print(users[0])
# Sandra
print(users[-1])
# John

print(users.index("Dave"))
# 1
print(users[0:2])
# ['Sandra', 'Dave'] because 2 exclude
print(users[1:])
# ['Dave', 'John']
print(users[-3:-1])
# ['Sandra', 'Dave']

print(len(data))
# 3

users.append("Elsa")
print(users)
# ['Sandra', 'Dave', 'John', 'Elsa']

users += ["Jason"]
print(users)
# ['Sandra', 'Dave', 'John', 'Elsa', 'Jason']

# /!\ don't forget the []
# users += 'Stan'
# print(users)
# # ['Sandra', 'Dave', 'John', 'Elsa', 'Jason', 'S', 't', 'a', 'n']

users.extend(["Robert", "Jammy"])
print(users)
# ['Sandra', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy']

# users.extend(data)
# print(users)
# # ['Sandra', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy', 'Sandra', 45, True]

# Insert at index = 0
users.insert(0, "Bob")
print(users)
# ['Bob', 'Sandra', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy']

# Insert at index = 2
users[2:2] = ["Eddie", "Alex"]
print(users)
# ['Bob', 'Sandra', 'Eddie', 'Alex', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy']

# Replace at index 1 et 2
users[1:3] = ["Gigi", "JP"]
print(users)
# ['Bob', 'Gigi', 'JP', 'Alex', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy']

users.remove("Bob")
print(users)
# ['Gigi', 'JP', 'Alex', 'Dave', 'John', 'Elsa', 'Jason', 'Robert', 'Jammy']

print(users.pop())
# Jammy
print(users)
# ['Gigi', 'JP', 'Alex', 'Dave', 'John', 'Elsa', 'Jason', 'Robert']

del users[0]
print(users)
# ['JP', 'Alex', 'Dave', 'John', 'Elsa', 'Jason', 'Robert']

# del data
# print(data)
# NameError: name 'data' is not defined

data.clear()
print(data)
# []

# users[1:2] = 'sandra'
# users.sort()
# print(users)
# ['Dave', 'Elsa', 'JP', 'Jason', 'John', 'Robert', 'a', 'a', 'd', 'n', 'r', 's']

# Insert gigi in first
users[1:2] = ["gigi"]
# then sort() = gig in last because in lowercase
users.sort()
print(users)
# ['Dave', 'Elsa', 'JP', 'Jason', 'John', 'Robert', 'gigi']

# Include lowercase in sort()
users.sort(key=str.lower)
print(users)
# ['Dave', 'Elsa', 'gigi', 'Jason', 'John', 'JP', 'Robert']

print()
print("***********************************")
print()

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
# [5, 1, 78, 42, 4]

# Reverse sort the original list
# nums.sort(reverse=True)
# print(nums)
# # [78, 42, 5, 4, 1]

# Reverse sort on a copy of the list
print(sorted(nums, reverse=True))
# [78, 42, 5, 4, 1] = non modified original list
print(nums)
# [5, 1, 78, 42, 4] = original list

# Create a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
print(mynums)
print(mycopy)
# all return [5, 1, 78, 42, 4]
# print(mycopy.sort()) return None because it print the instruction of sort, not the sorted list
mycopy.sort()
print(mycopy)
# [1, 4, 5, 42, 78]

print(type(nums))
# <class 'list'>

# Create a new list
mylist = list([1,"Neil",True])
print(mylist)
# [1, 'Neil', True]

# Tuple = list with fixed datas & fixed order
print()
print("TUPLES")
print()

# Tuple with constructor
mytuple = tuple(('Sandra',45,True))
print(mytuple)
# ('Sandra', 45, True)
print(type(mytuple))
# <class 'tuple'>

# Tuple without constructor
anothertuple = (1,4,2,8)
print(type(anothertuple))
# <class 'tuple'>

# Tuple copy
newlist = list(mytuple)
newlist.append('Gigi')
newtuple = tuple(newlist)
print(newtuple)
# ('Sandra', 45, True, 'Gigi')

# Unpack a tuple
(one, two, *hey) = anothertuple
print(one)
# 1 = fist value of anothertuple
print(two)
# 4 = 2nd value of anothertuple
print(hey)
# [2, 8] = rest of anothertuple because of * in front of hey
print(anothertuple)
# (1, 4, 2, 8)

# displays the list of available methods with : 
# print(anothertuple.), the list displays after the dot

# count the number of occurrences of a digit
print(anothertuple.count(2))
# 1







