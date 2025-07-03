#Q.1 Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class
#answr
class MyClass:
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            print("Default constructor called")
        elif y is None:
            print(f"One-argument constructor called with x={x}")
        else:
            print(f"Two-argument constructor called with x={x}, y={y}")

# Main section
obj1 = MyClass()          # Calls default constructor
obj2 = MyClass(10)        # Calls one-argument constructor
obj3 = MyClass(10, 20)    # Calls two-argument constructor

#Q.2 Call the constructors(both default and argument constructors) of super class from a child class
#answr
class Parent:
    def __init__(self, x=None):
        if x is None:
            print("Parent default constructor")
        else:
            print(f"Parent parameterized constructor with x={x}")

class Child(Parent):
    def __init__(self, x=None):
        if x is None:
            super().__init__()        # Call Parent's default constructor
        else:
            super().__init__(x)       # Call Parent's parameterized constructor

# Testing
Child()          # Calls Parent default constructor
Child(10)        # Calls Parent parameterized constructor


#Q.3  Apply private, public, protected and default access modifiers to the constructor
#answr
class MyClass:
    def __init__(self):              # Public constructor
        print("Public (default) constructor")

    def _protected_init(self):       # Protected-like constructor (convention)
        print("Protected constructor")

    def __private_init(self):        # Private-like constructor (name mangling)
        print("Private constructor")

# Usage
obj = MyClass()                      # Calls public constructor
obj._protected_init()                # Accessible but intended as protected
obj._MyClass__private_init()         # Access private constructor using name mangling

#Q.4 Write a program which illustrates the concept of attributes of a constructor.
#answr
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Attribute for car make
        self.model = model    # Attribute for car model
        self.year = year      # Attribute for car year

c = Car("Honda", "Civic", 2020)
print(c.make, c.model, c.year)
