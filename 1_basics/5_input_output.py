"""
Output : print()
| Parameter | Description                                        |
| --------- | -------------------------------------------------- |
| `sep`     | Separator between items (default is space)         |
| `end`     | What to print at the end (default is newline `\n`) |

"""
print("A", "B", "C", sep="-")   # A-B-C
print("Hello", end="!")        # Hello!
# here newline is not added as `end` is not set to '\n'


"""
Input : input(prompt)
 -> it always returns string so make sure to convert it to appropriate data type
"""
x = input("Enter your name : ")
print(type(x)) # output : <class 'str'>
