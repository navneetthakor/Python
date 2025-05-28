"""
if else statement
"""
myname = "Navneet"
id = 24

if id > 31:
    if myname:
        print(myname)
    else:
        print("Name is not present")
elif id == 24:
    print("name is meet joshi")
else:
    print("Id is not greater then 31")


"""
Match-case statement:
    -> it is equvalant to switch-case of other languages like javascript,java,c++,C# etc.
"""

match(id):
    case 31 if myname.lower() == "navneet":
        print("name is navneet")
    case 33:
        print("name is Rohanshu")
    case 34 | 40:
        print("Name is Raag joshi")
    case 24 | 305 if myname.lower() == "navneet":
        print("name is meet")
    case _: # default case
        print("id is not valid")