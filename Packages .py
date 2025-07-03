#Q.1 Create a program to create two class.
#answr

class Car:
    def drive(self):
        print("Car is driving")

class Bike:
    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()
car.drive()
bike.ride()


#Q.2 Create a constructor and a method for each class
#answr
class A:
    def __init__(self, x):
        self.x = x
    def display(self):
        print(f"Value in A: {self.x}")

class B:
    def __init__(self, y):
        self.y = y
    def show(self):
        print(f"Value in B: {self.y}")

a = A(10)
b = B(20)
a.display()
b.show()

# Q.3 Create a __init__.py for adding all packages
#answr
# __init__.py
# creat my_Allpackage file

# __init__.py
from My_Allpackage.fuctions import adder
from My_Allpackage.more_fuctions import subtractor
#from My_Allpackage.module1.module2.module3.trigo_fuction import sine
# using __init__.py
from My_Allpackage import sine
adder(20 , 20)
subtractor(2 , 30)
sine()

#Q.4 Import the respective packages
#answr

from My_Allpackage.math_fuction import sqrt, pi
print(sqrt(16))
print(pi)

#Q.5  Call each class by creating an object to it
#answr
class A:
    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C:
    def greet(self):
        print("Hello from class C")

# Creating objects of each class
a_obj = A()
b_obj = B()
c_obj = C()

# Calling method using each object
a_obj.greet()
b_obj.greet()
c_obj.greet()


Q.6#  Create a program by all the above
#answr
class A:
    def __init__(self): self.x = 1
    def show(self): print(f"A: {self.x}")

class B:
    def __init__(self): self.y = 2
    def display(self): print(f"B: {self.y}")

class C:
    def __init__(self): self.z = 3
    def greet(self): print(f"C: {self.z}")

a, b, c = A(), B(), C()
a.show()
b.display()
c.greet()
