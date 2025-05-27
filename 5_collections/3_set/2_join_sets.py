"""
There are several ways to join sets
"""

# 1) union() or |
# returns union of both sets (not modify any present set)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #output : {1, 2, 'a', 3, 'c', 'b'}

# multiple set joining 
set4 = set3.union(set1,set2)
print(set4)
set4 = set3 | set1 | set2

# -> only difference between `union()` and `|` is that 
    # -> union() can be work with any iterator while `|` only with sets 

# 2) udpate()
# adds value from set2 to set1
set1.update(set2)
    # -> works with any iterable 
print(set1)

# 3) intersection() and &
set3 = set1.intersection(set2)
print(set3)
    # ->  The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.

# 4) intersection_update()
set1.intersection_update(set2)

# 5) difference
# will return a new set that will contain only the items from the first set that are not present in the other set.
set4 = set3.difference(set1)

# 6) diffrerenct_update()
set3.difference_update(set4)