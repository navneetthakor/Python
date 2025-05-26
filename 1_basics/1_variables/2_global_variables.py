#using global variable

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() # output : "Python is awesome"





# local variable (works fine)
def myfunc():
  x = "nk"
  print("Python is " + x)

myfunc() # output : "Python is nk"






# local variable (works fine)
# def myfunc():
#   print("Python is " + x)
#   x = "nk"

# myfunc() # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value



# declaring global variable from function
def myfunc():
  global y
  y = 'ok'
  print("Python is " + y)

myfunc()
print(y)


# manipulating global variable from function
def myfunc():
  global x
  x = 'manipulate'
  print("Python is " + x)

myfunc()
print(x)