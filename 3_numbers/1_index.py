# basic things are already covered like conversion, types identification, etc.
"""
python is very powerful when it comes to working with numbers
"""

# math library
import math

math.floor(3.3) # output : 3
math.ceil(3.3) # output : 4

# bases ---
print(0o120) # octal
print(0x120) # hexa
print(0b0001) # binary

# reverse to bases
print(oct(80))
print(hex(288))
print(bin(1))

#base using int()
print(int('64',8))


# random number
import random
print(random.random()) # random number between 0 to 1
print(random.randint(1,100)) # in range of 1 to 100

# sets are also treated as numbers
seta = {1,2,3}
setb = {2,3,4}
print(seta - setb)
# print(seta + setb) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(seta * setb) # TypeError: unsupported operand type(s) for *: 'set' and 'set'
print(seta | setb)
print(seta & setb)