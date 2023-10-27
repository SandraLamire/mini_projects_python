# Dictionaries = key,value pairs
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# Using dictionary constructor
band2 = dict(vocals="Plant", guitar="Page")

print(band)
# {'vocals': 'Plant', 'guitar': 'Page'}
print(band2)
# {'vocals': 'Plant', 'guitar': 'Page'}
print(type(band))
# <class 'dict'>
print(len(band))
# 2

# Access items
print(band["vocals"])
# Plant
print(band.get("guitar"))
# Page

# List all keys
print(band.keys())
# dict_keys(['vocals', 'guitar'])

# List all values
print(band.values())
# dict_values(['Plant', 'Page'])

# List of key/value pairs as tuples
print(band.items())
# dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# Verify a key exists
print("guitar" in band)
# True
print("triangle" in band)
# False

# Change values
band ["vocals"] = "Coverdale"
print(band["vocals"])
# Coverdale (instead of Plant)
band.update({"bass": "JP"})
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JP'}

# Remove items
print(band.pop("bass"))
# JP
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page'}
band["drums"] = "Bonham"
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}
print(band.popitem())
# ('drums', 'Bonham') = tuple

# Delete and clear
band["drums"] = "Bonham"
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Bonham'}
del band["drums"]
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page'}

# Empty dictionary
band2.clear()
print(band2)
# {}

# Delete empty dictionary
del band2

# Copy dictionaries

# # /!\ Create a reference = band & band2 point to the same reference
# band2 = band 
# print("Bad copy!")
# # because band = band2
# print(band2)
# print(band)
# # {'vocals': 'Coverdale', 'guitar': 'Page'}

# band2["drums"] = "Dave"
# print(band)
# # {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}
# # because band = band2

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
# {'vocals': 'Coverdale', 'guitar': 'Page'}
print(band2)
# {'vocals': 'Coverdale', 'guitar': 'Page', 'drums': 'Dave'}

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)
# {'vocals': 'Coverdale', 'guitar': 'Page'}

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2,
}
print(band)
# {'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
print(band["member1"]["name"])
# Plant

print('***********************')
# sets (= ensembles)
nums = {1, 2, 3, 4}
print(nums)
# {1, 2, 3, 4}
nums2 = set((1,2,3,4))
print(nums2)
# {1, 2, 3, 4}
print(type(nums))
# <class 'set'>
print(len(nums))
# 4

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)
# {1, 2, 3}

# True is a dupe of 1, False is a dupe of 0
nums =  {1, True, 2, False, 3, 4, 0}
print(nums)
# {False, 1, 2, 3, 4}

# Check if a value is in a set
print(2 in nums)
# True

# /!\ But you cannot refer to an element in the set
# with an index position or a key!

# Add a nnew element to a set
nums.add(8)
print(nums)
# {False, 1, 2, 3, 4, 8}

# Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)
# {False, 1, 2, 3, 4, 5, 6, 7, 8}

# You can use update with lists, tuples and dictionaries too

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)
# {1, 2, 3, 5, 6, 7}

# Keep only the duplicates
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)
# {2, 3}

# Keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)
# {1, 4}










