"""
Inheritance : the process through which we can create new class from the existing class. 
Types inheritance :
    - single
    - Multiplevel 
    - Hybrid
    - Multiple
    - Hierarchical

super()
    -> here super returns objects represented in the parent’s class and enables multiple inheritances.
"""

"""
Single inheritance
"""
class Parent:
    def __init__(self, name):
        self.name = name
    
    def print_data(self):
        print(f"Name is {self.name}")


# drived class
class Single_Inheritance(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def print_data(self):
        super().print_data()
        print(f"Age is {self.age}")

# create object 
single_inheritance_obj = Single_Inheritance("Navneet",21)
single_inheritance_obj.print_data()


"""
Multilevel inheritance
"""
class Multilevel_Inheritance(Single_Inheritance):
    def __init__(self, name, age):
        super().__init__(name, age)
        print("\nMultilevel object -> init method")

    def print_data(self):
        super().print_data()

multilevel_inheritance_obj = Multilevel_Inheritance("Navneet",21)
multilevel_inheritance_obj.print_data()


"""
Simillarly other inheritance like : multiple, hybrid, hierarchical
"""

"""
to check relationship of two classes and instances
"""
# issubclass(sub, sup)
print(issubclass(Multilevel_Inheritance,Parent)) # output : true

# isinstance(obj, Class) 
print(isinstance(multilevel_inheritance_obj,Parent)) # output : true


"""
Why class attributes are directly accesseble by object of that class
    -> When you access obj.attr:
        -> Python looks in the instance’s __dict__.
        -> If not found, it looks in the class’s __dict__.
        -> If still not found, it continues up the inheritance chain (parent classes).
"""

"""
| Concept       | Meaning                                 | Example                      | Purpose                    |
| ------------- | --------------------------------------- | ---------------------------- | -------------------------- |
| Polymorphism  | One interface, multiple implementations | `speak()` in `Dog` and `Cat` | Flexible & generic coding  |
| Encapsulation | Hide internal state, access via methods | `__balance` in `BankAccount` | Data protection and safety |

"""