"""
List items are ordered, changeable, and allow duplicate values.
"""
# define string
myFrnds = ['RB', 'Meet', 'Hina', 'Maulik', 'RB']

# lengh of list
print(len(myFrnds)) # output : 5

# accessing values and slicing
# print(myFrnds[20]) # index outof range error
print(myFrnds[-1])
print(myFrnds[20:50]) # slicing want give you error even if it's out of range

# check if item exits
print("RB" in myFrnds)