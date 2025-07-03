#Q.1 Create an abstract class with abstract and non-abstract methods.
#answr
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self): pass  # Abstract method

    def concrete_method(self):       # Non-abstract method
        print("This is a concrete method")

class ConcreteClass(MyAbstractClass):
    def abstract_method(self):
        print("Implementation of abstract method")

obj = ConcreteClass()
obj.abstract_method()
obj.concrete_method()

#Q.2 Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods
#answr
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def abs_m(self): pass
    def non_abs_m(self): print("Non-abstract method")

class B(A):
    def abs_m(self): print("Implemented abstract method")

B().non_abs_m()

#Q.3 Create an instance for the child class in child class and call abstract methods
#answr
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def abstract_m(self): pass

class B(A):
    def abstract_m(self):
        print("Implemented abstract method")
    def call_self(self):
        B().abstract_m()  # create instance and call abstract method

B().call_self()


#Q.4 Create an instance for the child class in child class and call non-abstract methods
#answr
from abc import ABC, abstractmethod

class A(ABC):
    def non_abstract(self):
        print("Non-abstract method in A")

    @abstractmethod
    def abstract_m(self): pass

class B(A):
    def abstract_m(self):
        print("Implemented abstract method in B")

    def call_self(self):
        B().non_abstract()  # create instance and call non-abstract method

B().call_self()
