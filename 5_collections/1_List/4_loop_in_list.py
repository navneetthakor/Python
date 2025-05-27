myFrnds = ['RB', 'Meet', 'Hina', 'Maulik', 'RB']

# 1st option 
for frnd in myFrnds:
    print(frnd, end=", ")
print()

#2nd option
for index in range(len(myFrnds)):
    print(myFrnds[index], end=", ")
print()

# 3th while loop
index = 0 
while index < len(myFrnds):
    print(myFrnds[index], end=", ")
    index += 1
print()


#4rd option (comprehensive)
[print(frnd, end=", ") for frnd in myFrnds]
print()


"""
List comprehension : it offers a shorter syntax when you want to create a new list based on the values of an existing list.
Syntx:
    newlist = [expression for item in iterable if condition == True]

"""
newFrnds = [frnd for frnd in myFrnds if frnd.__contains__('R')]
print(newFrnds)
