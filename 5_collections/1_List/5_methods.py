myFrnds = ['RB', 'Meet','hina', 'Maulik', 'RB']
items = [1,2,3,4,5]

"""
Sorting
 -> sort() wont work if int and str both present together in the list
 -> there is work around this issues is we can do like this `lst.sort(key=str)`
"""
# sorts alphabetically
myFrnds.sort() 
print(myFrnds)

# reverse order
myFrnds.sort(reverse=True)
print(myFrnds)

#customize sort function
def myFunc(ele):
    return abs(50-ele)
items.sort(key=myFunc)
print(items) # output : [5, 4, 3, 2, 1]

"""
 case-insensitive sorting:
    -> by default sort function is case sensitive so in string all the uppercase will come first before lowwer case
    -> for case-insensitive sorting we can use str.lower key
"""
myFrnds.sort(key=str.lower)
print(myFrnds)


"""
To reverse list
"""

myFrnds.reverse()
print(myFrnds)

"""
Copy list :
    -> we can't copy list by simply doing lst1 = lst2 as now both of this are pointing to the same reference instead of creating new copy
    -> so below are some ways
"""

# unwanted behaviour 
copyFrnds = myFrnds
print(copyFrnds is myFrnds)

# 1st
copyFrnds = myFrnds.copy()
print(copyFrnds is myFrnds)

# 2nd 
copyFrnds = list(myFrnds)
print(copyFrnds is myFrnds)

# 3rd 
copyFrnds = myFrnds[:]
print(copyFrnds is myFrnds)

# 4th (using copy module)
import copy
copyFrnds = copy.copy(myFrnds)
print(copyFrnds is myFrnds)

# also supports deepcopy 
copyFrnds = copy.deepcopy(myFrnds) # list inside list then use this one
print(copyFrnds is myFrnds)

"""
join lists
"""

# 1st (usinig + operator)
newList = copyFrnds + myFrnds
print(newList)

# 2nd (using any loop)
[copyFrnds.append(frnd) for frnd in myFrnds]
print(copyFrnds)

#3rd using extend method
copyFrnds.extend(myFrnds)
print(copyFrnds)
