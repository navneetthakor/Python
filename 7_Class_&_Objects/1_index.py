"""
Class is blueprint to create object, while object is instance of this class
"""

# basic class structure
class My_class:
    """
    optional documentation string
    """
    pass

# to access documentation string
print(My_class.__doc__)


"""
Employee class for understanding 
 - class structure
 - object creation
 - class variable
 - instance variable
 - constructor
 etc...
"""

class Employee:
    """
    This is Employee class
    """
    # class variable 
    emplyCount = 0

    # constructor 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emplyCount += 1
        hero = "naveet"

    # destructor 
    def __del__(self):
        """
        -> invoked when the instance is about to be destroyed
        -> used to clean up any non-memory resources used by an instance.
        """
        print("destroying object")
        Employee.emplyCount -= 1
    
    # methods
    def displayEmplyCount(self):
        print(f"Employee count is {Employee.emplyCount}")

    def displayEmployee(self):
        print(f"Name : {self.name}      salary: {self.salary}")

# create object of class
emply = Employee("Navneet", "7,00,000")

# access instance method and variables 
emply.displayEmployee()
emply.displayEmplyCount()


# add attribute to object at run time
emply.emplyCount = 5
print(emply.emplyCount)  # instance attribute : 5
print(Employee.emplyCount)  # class attribute : 1

# modify value of attribute
emply.name = "Navneetkumar"

#delete attribute
del emply.emplyCount
print(emply.emplyCount) # class attribute : 1


"""
Functions for class attributes
"""
# except hasattr,and setattr, everyone else will throgh error if attrib not present
print(hasattr(emply,"age")) # output: false
print(getattr(emply,"salary")) # output: 7,00,000
setattr(emply,'age',21)
print(emply.age)
delattr(emply,'age')
# print(emply.age) #output : error


"""
buil it class attribute
"""
# prints class's namespace
print(Employee.__dict__) # output : everything is present about class
print(emply.__dict__) # output : {'name': 'Navneetkumar', 'salary': '7,00,000'}

# documentation string
print(Employee.__doc__) #output: This is Employee class
print(emply.__doc__) #output: This is Employee class

# class name
print(Employee.__name__) #output: Employee
# print(emply.__name__) #output: <ERROR>


