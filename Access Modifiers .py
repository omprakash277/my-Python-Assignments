# Q.1 Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.
#answr
class MyClass:
    def __init__(self): self.__data = "Private Data"
    def __private_method(self): print("This is a private method")
    def main(self):
        print(self.__data)
        self.__private_method()

MyClass().main()

#2 Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.
# answr
class A:
    def __init__(self): self._data = "Protected data"
    def _protected_method(self): print("Protected method called")

class B:
    def access(self):
        a = A()
        print(a._data)
        a._protected_method()

B().access()


#Q.3 Create a class with PUBLIC fields and methods.
#answe
class MyClass:
    def __init__(self, name, age):
        self.name = name           # Public field
        self.age = age             # Public field

    def display(self):              # Public method
        print(f"Name: {self.name}, Age: {self.age}")

obj = MyClass("Alice", 30)
obj.display()
