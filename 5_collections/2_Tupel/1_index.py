"""
A tuple is a collection which is ordered, unchangeable, and allows duplication.
"""

#create tuple example 
frnds = ('RB', 'Meet')
item = tuple(("nk", "Rohanshu"))
itme2 = tuple((1 ,)) # When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

#tuple length
print(len(frnds)) # output : 2

# access value and slicing
print(frnds[0])
print(frnds[-2:])

# wheather value present in the tupel or not
print(1 in item) # false
print("nk" in item) # true


"""
updating tuple
"""
# adding value
# 1st option (convert to list then add and again convert back to tuple)
# 2nd option (we can add two tuples and create new one)
total_item = item + itme2
print(total_item)

# revome value
# 1st option (convert to list then remove and again convert back to tuple)
# 2nd option (use del operator to delete whole tuple)
del itme2
# print(itme2) #this will raise an error because the tuple no longer exists


"""
unpack tuple
"""
item = (1,2,3,4)

#equal number of varible as values in tuple
x,y,z,w = item
print(z)

#less variable then value
x,y,*z = item
    # -> here Z has remaining values as list

x,*y,z = item
    # -> here y has value that are remaining after allocating values to othe variables
    # x = 1, y = [2,3], z = 4

"""
Join tuples
"""
#1st using + operator (as seen above)
#2nd muliply
print(item*3) # output : (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)


