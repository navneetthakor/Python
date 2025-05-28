"""
For loop:
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
"""
my_name = "navneet"

for char in my_name:
    print(char, end="")
print() # just to add line at the end


# break : to terminate loop at middle
# continue : to skip current iteration
# pass : just a space holder in abasence of the content to avoid compile time errors
# else bolck: will executed if loop is terminated normally (not by break or something else)

for char in my_name:
    if char == 'k':
        break;
    else:
        continue;
else:
    print("Loop termintated normally")

# range function : retuns range of sequances
    # -> 3 variations
        # -> (end) : 0 to end -1
        # -> (start,end) : start to end -1
        # -> (start,end,step) : start to end-1 but it += step
for it in range(6): print(it, end="-") # output 0-1-2-3-4-5-


"""
While loop:
    -> same as other languages and has attributes discussed about for loop except range()
"""
it=0
while it < 5:
    print(it)
    it+=1
    # break
else:
    print("While loop completed properly")