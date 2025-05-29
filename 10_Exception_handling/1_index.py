"""
Exception is an event that can occur during the execution of the program,
that disrupts the normal flow of the program.
"""


isExceptionThrown = False

try:
    x = "navneet"
    if(isExceptionThrown): raise Exception("bad writting")

except IOError as ex:
    print('IOError exception',ex)

except (SystemError,SyntaxError) as ex:
    print("Grouped exceptions", ex)

except Exception as ex: # this generic exception block must be place after all the other exception blocks
    print('Generic exception',ex)

else:   # execute if no exceptions will thrown
    print("No exception was thrown")

finally:
    print("Will always executed regarless of exception is raised or not")

"""
There are many types of exceptions are present in python all of those are mention in the pdf present in this folder
""" 

"""
Assertion : 
    -> use in development to raise exception upon certain condition meets
    -> if result is false raise assertion
"""

is_raise_assertion = True
assert (is_raise_assertion), "throwing assertion"


"""
Custom Exception by inheriting exception classes
"""

class My_Exception(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.args = args


is_cusomt_exception = True

try:
    x = "navneet"
    if(is_cusomt_exception): raise My_Exception("Custom exception")

except My_Exception as ex:
    print('Custom exception : ',ex)
    print(ex.args)

else:   # execute if no exceptions will thrown
    print("No exception was thrown")

finally:
    print("Will always executed regarless of exception is raised or not")

