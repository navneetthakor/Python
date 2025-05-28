# simple function signature
def func():
    print("Sample function")

#call function 
func()

"""
Functions have different arguments types as explained below
"""

# 1) positional arguments
def func1(name,age):
    print(name,age)
func1("navneet",21) # must follow the order of parameters

# 2) keyword arguments
func1(age=21,name="navneet") # can be write in any order

# 3) default arguments
def func2(name,age=31):
    print(name,age)

# both of below will work fine
func2("navneet")
func2("navneet",33) 

# 4) variable length input (converts to tupel form)
def func3(*args):
    print(type(args))   # output: <class 'tuple'>
    print(len(args))
    if len(args): print(args[0])

func3("Hello brother",25,86,"RB")

# 5) **kwargs – Keyword Variable Arguments
# Collects extra keyword arguments as a dictionary.
def func4(**args):
    print(type(args))   # output: <class 'dict'>
    print(len(args))
    if len(args): print(args["name"])

func4(name="Hello brother",eid=421) #must be keyword

"""
We can use mixture of all of the above arguments type but we have to follow order as below:
def func(
    pos_only,           # 1. Positional-only arguments (Python 3.8+ using /)
    pos_or_kwd,         # 2. Positional-or-keyword arguments
    kwd_only,           # 3. Keyword-only arguments
    *args,              # 4. Variable-length positional arguments
    **kwargs            # 5. Variable-length keyword arguments
)
"""


"""
return values
"""

def retrnFunc():
    return ["navneet","421"]

print(retrnFunc())