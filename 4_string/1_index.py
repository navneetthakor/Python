"""
Strings are Arrays : 
-> Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
-> However, Python does not have a character data type, a single character is simply a string with a length of 1.
"""

name = "navneet"

# first char
print(name[0])

#slicing
print(name[1:3]) # 'av'
print(name[:]) # 'navneet'
print(name[:4]) # 'nav'
print(name[2:]) # 'vneet'
print(name[0:5:2]) # 'nve'

#methods
# lowwer()
# upper()
# strip() # remove space from end and start
result = name.replace('ee','i')
print(result)

a = "nk,meet,eb,hina"
print(a.split("c")) # if split operator not found then entire string at first location
print(a.find('me')) # -1 if not found
print(a.count('e'))

#string manipulation
# 1st way
print("my name is {}".format(name))
# 2nd way
print(f"my name is {name}")

#list to string
print("-".join(a.split(",")))

# lenght of string
print(len(a))

# escap character
print("navneet\nthakor")
print("navneet\\nthakor")
print(r"navneet\nthakor") # -> raw form of string
#output
    # navneet
    # thakor
    # navneet\nthakor
    # navneet\nthakor

# membership operator
print("ee" in "navneet") # true
print("ee " in "navneet") # false
