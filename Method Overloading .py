#Q.1 Write two methods with the same name but different number of parameters of same typeand call the methods
#answr
class Example:
    def add(self, a, b=None):
        print(a + b if b is not None else a)

obj = Example()
obj.add(5)       # Output: 5
obj.add(5, 10)   # Output: 15

#Q.2 Write two methods with the same name but different number of parameters of different data type and call the methods
# answr

class Example:
    def display(self, x):
        if isinstance(x, int):
            print(f"Integer: {x}")
        elif isinstance(x, str):
            print(f"String: {x}")

obj = Example()
obj.display(10)      

#Q.3 Write two methods with the same name and same number of parameters of same type
#answr
class Example:
    def greet(self, name):
        print(f"Hello, {name}!")

obj = Example()
obj.greet("OM")
