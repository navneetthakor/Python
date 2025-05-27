# basic things are already covered like conversion, types identification, etc.
"""
- python is very powerful when it comes to working with numbers
- there are three numeric types in python
    int,
    float,
    complex
"""

"""
int : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    - means here the limit of int is only bounded by availabel memory
"""

#type conversion
a = 1
b = 1.1
c = 2 + 3j
print(float(a)) # 1.0
print(int(b)) # 1
print(complex(a)) # (1+0j)
print(complex(b)) # (1.1+0j)
# print(int(c)) # error
# print(float(c)) # error

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

"""
sets : sets are also treated as numbers
"""
