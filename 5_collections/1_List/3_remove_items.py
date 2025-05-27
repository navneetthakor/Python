"""
following are the differente ways to remove items from tuples
"""

items = [1,2,3,4,5, ['nk']]

# remove by content (uses == internally)
items.remove(['nk'])
print(items)

#remove by id (two options)
# 1st 
items.pop() # removes last item (as default index is set to -1)
items.pop(2) # removes item at location 2
print(items)

# 2nd 
del items[0]
print(items)

# del can also delete whole list
# del items # uncomment this line (by nk not chatgpt ok)
print(items) # NameError: name 'items' is not defined

# to clear the content of list
items.clear()