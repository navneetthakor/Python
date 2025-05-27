myFrnds = ['RB', 'Meet', 'Hina', 'Maulik', 'RB']

myFrnds[0] = "Shaurya"
myFrnds[0:1] = ['RB','KK','SS'] # If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

# insert item 
myFrnds.insert(5,'RJ') # insert at 5th location
myFrnds.append('RK') # append at last
print(myFrnds)

temp = [1,2]
myFrnds.extend(temp) # merge another list to current list
print(myFrnds)
temp = "nk"
myFrnds.extend(temp) # extend() can merge any iterable
print(myFrnds)
