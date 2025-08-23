# Dictionaries
band = {
    "Vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band2))
print(len(band2))

# Accessing values
print(band["Vocals"])
print(band.get("guitar"))

# List of all keys
print(band.keys())

# List of all values
print(band.values())

# List of all items keys/value pairs as Tuples
print(band.items())

# verify if a key exists
print("guitar" in band)
print("triangle" in band)

#change values 
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print("bass")

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)
#dict(constructer function)
band2.clear()
print(band2)

del band2

# copying dictionaries

# band2 = band # Create a reference
# print("Bad Copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy !")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy !")
print(band3)

# Nested dictionaries

member1 = {
    "name ": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name ": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
# print(band["member1"] ["name"])

# Sets

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed

nums = {1,2,2,4}
print(nums)

# True is a dupe of 1, False is a dupe of zero.
nums = {1,True,2,False,3,4,0} 
print(nums)

# Check if a value is a set.

print(2 in nums)


# But you cannot refer to an element 
# in the set eith an index position or key

# Add a new element to a set.
nums.add(8)
print(nums)

# Add a Element from one set to another.
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# You can use updates with lists,tuples and dictionaries,
#too.

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates.
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates.
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)