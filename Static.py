#Q.1 Define a static variable and access that through a class
#answr
class Student:
    count = 0  # static variable

    def __init__(self, name):
        self.name = name
        Student.count += 1  # accessing and modifying static variable

# Creating instances
student1 = Student("om")
student2 = Student("prakash")

# Access static variable via class
print("Number of students:", Student.count)

# Access static variable via instance (not recommended)
print("student1 count:", student1.count)

# Q.2 Define a static variable and access that through a instance
# answr
class MyClass:
    static_var = 100  # static (class) variable

# Create an instance
obj = MyClass()

# Access static variable through instance
print("Access via instance:", obj.static_var)

# Q.3 Define a static variable and change within the instance
#answr
class MyClass:
    static_var = 100  # static (class) variable

# Create two instances
obj1 = MyClass()
obj2 = MyClass()

# Access static variable via class and instances
print("Initial values:")
print("MyClass.static_var:", MyClass.static_var)
print("obj1.static_var:", obj1.static_var)
print("obj2.static_var:", obj2.static_var)

# Change static_var via obj1 instance
obj1.static_var = 200

print("\nAfter changing obj1.static_var to 200:")
print("MyClass.static_var:", MyClass.static_var)
print("obj1.static_var:", obj1.static_var)
print("obj2.static_var:", obj2.static_var)

#Q.4 Define a static variable and change within the class
#answr

class MyClass:
    static_var = 10  # static (class) variable

    @classmethod
    def change_static_var(cls, value):
        cls.static_var = value  # modify static variable using cls

# Access static variable before change
print("Before change:", MyClass.static_var) 
# Change static variable using class method
MyClass.change_static_var(50)

# Access static variable after change
print("After change:", MyClass.static_var)
