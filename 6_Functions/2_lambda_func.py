"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
    -> se lambda functions when an anonymous function is required for a short period of time.
"""

my_multiplier = lambda x : x*2
print(my_multiplier(54))

full_name = lambda fname,lname : f"Hello Mr. {fname.capitalize()} {lname.capitalize()}"
print(full_name("navneet","Thakor"))

