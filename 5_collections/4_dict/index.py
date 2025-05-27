"""
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    -> As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

# create dictionary
# here `key` can be any hashable (immutable) data type like str, int, tuple, boolean etc 
dict1 = {
    "name": "Navneet",
    "gender" : "boy"
}
print(dict1)

dict2 = dict([["name","navneet"],["gender","boy"]])
print(dict2)

dict3 = dict(name="navneet",gender="boy")
print(dict3)


# length of dictionary
print(len(dict3)) #output : 2

"""
Accessing items
"""

# 1) access value 
print(dict1["name"])

# 2) get all keys as list
lstKeys = dict1.keys()
print(lstKeys)

dict1['bdyear'] = 2003
print(lstKeys) # keys list get automatically updated by adding `bdyear` here

# 3) get all values as list
lstValues = dict1.values()
print(lstValues)

dict1["gender"] = 'Male'
print(lstValues) # Values list get automatically updated by adding `bdyear` here

# 4) get list tuples as key value pair 
tplKeyValues = dict1.items()
print(tplKeyValues)

dict1['games'] = 'cricket'
print(tplKeyValues) # gets automatically updated

"""
check if key exists in dict by using mebmership operator directly on to the dictionary
"""

"""
add or update items in dict
"""
# 1) using []
dict1["games"] = "Chess" #update
dict1["company"] = "RKIT" # add
print(dict1)

# 2) update()
dict1.update({
    "team" : "Auto projects", # add
    "games" : "cricket"
}) # accepts dictionary or iterable in key:value form
print(dict1)

"""
Remove items form dict
"""
print("------------ remvoe items -------------------")
#removes lastly added item
item = dict1.popitem() 
print(item) 

 # remove item based on provided key
item = dict1.pop("games")
print(item)

 # removes items with specified key
print(dict2)
del dict2["name"]
print(dict2)

#makes dictionary empty
dict2.clear() 
print(dict2)

