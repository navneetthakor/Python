"""
A set is a collection which is unordered, unchangeable*, and unindexed.
    -> Set items are unchangeable, but we can remove items and add new items.
    -> duplicates not allowed
"""

# create set (see duplicates not allowed)
mset = {1,2,3,1,1,True,False,0}
mset2= set((1,2))
print(mset) # output : {False, 1, 2, 3}

"""
PITFALLS:
    -> value True and 1 is treated as same
    -> value False and 0 is treaed as same
"""


"""
access items in set:
    -> we can't really access set values by index or key
    -> only option that we left is by using loop on set
"""
[print(x, end="-") for x in mset]
print()

# item is present in set or not
print(False in mset)
print(False not in mset)

"""
Add items in set
"""
# 1st using add()
mset.add(5)
print(mset)

# add set with any iterable (set, list, string,tuple)
mset.update(mset2)
print(mset)


"""
Remove items form set
"""
# 1st using remove()
mset.remove(1) 
    # -> here 1 is value that i want to remove
    # -> if 1 is not present in the set then it will raise Exception

# 2nd using discard()
mset.discard(1) 
    # -> here 1 is value that i want to remove
    # -> if 1 is not present in the set then it will `NOT` raise Exception

# 3rd using pop() but it will remove random item
mset.pop()

#4th clear() to empty whole set
mset.clear()

#5th del operator to delete set entirely
del mset

"""
 noraml operations on set
"""
seta = {1,2,3}
setb = {2,3,4}
print(seta - setb) # except operation
# print(seta + setb) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(seta * setb) # TypeError: unsupported operand type(s) for *: 'set' and 'set'
print(seta | setb) # or operaton
print(seta & setb) # and operation


#not allowed
print({{"navneet": "mayur"}} - {{"navneet": "mayur"}})

"""
we cannot use list, dict, or other mutable types inside a set
->  Reason:
Python sets require all elements to be hashable.
But mutable types are not hashable, because their contents can change — breaking the rules of how sets/dictionaries track uniqueness.

-> work around by using fronzenset, json.dump() [convert to string]
🧾 Summary:
Type	    Mutable	Hashable	Can be in Set?
list	    ✅	    ❌	    ❌
dict	    ✅	    ❌	    ❌
set	        ✅	    ❌	    ❌
tuple	    ❌	    ✅	    ✅
frozenset	❌	    ✅	    ✅
str	        ❌	    ✅	    ✅
numbers	    ❌	    ✅	    ✅ (int, float, complex)
"""