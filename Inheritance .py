# (1.Q)  A, B and C are classes
#answr
class A: pass
class B(A): pass
class C(A): pass

b = B()
c = C()
print(isinstance(b, A), isinstance(c, A))

#Q.2 A is a super class. B is a sub class of A. C is a sub class of B.
#answr
class A:
    def show_a(self):
        print("This is class A")

class B(A):
    def show_b(self):
        print("This is class B")

class C(B):
    def show_c(self):
        print("This is class C")

obj = C()
obj.show_a()  # Inherited from A
obj.show_b()  # Inherited from B
obj.show_c()  # Defined in C

#Q.3 Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C
#answr
class A:
    def specific_a(self): print("A specific method")
    def override_method(self): print("Override in A")

class B(A):
    def specific_b(self): print("B specific method")
    def override_method(self): print("Override in B")

class C(B):
    def specific_c(self): print("C specific method")
    def override_method(self): print("Override in C")

c = C()
c.specific_c()
c.override_method()

#Q.4 Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.
#answr
class A:
    def m1(self): print("A m1")
    def m2(self): print("A m2")
class B:
    def m1(self): print("B m1")
    def m2(self): print("B m2")
class C:
    def m1(self): print("C m1")
    def m2(self): print("C m2")

def main():
    a, b, c = A(), B(), C()
    a.m1(); a.m2(); b.m1(); b.m2(); c.m1(); c.m2()

if __name__ == "__main__":
    main()

#Q.5 Call an overridden method with super class reference to B and C class’s objects
#answr
class A:
    def show(self): print("A's show")
class B(A):
    def show(self): super().show(); print("B's show")
class C(B):
    def show(self): super().show(); print("C's show")

b = B(); c = C()
b.show()
c.show()

# Q.6 Runtime Polymorphism with Data Members/Instance variables, Repeat the above  process only for data members
#answr
class A:
    def __init__(self): self.val = 10
class B(A):
    def __init__(self): self.val = 200
class C(B):
    def __init__(self): self.val = 300

for obj in (B(), C()):
    print(obj.val)
