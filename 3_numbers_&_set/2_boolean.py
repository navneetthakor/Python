"""
boolean are also treated as number internally
"""

# False: if 0, 0.0, '',{}, [], None : else true
print(bool({})) # use this function for conversion

"""
Easy rule for conversions:
-> Almost any value is evaluated to True if it has some sort of content.
-> Any string is True, except empty strings.
-> Any number is True, except 0.
-> Any list, tuple, set, and dictionary are True, except empty ones.
-> if clss have `__len__()` and that returns 0
"""
