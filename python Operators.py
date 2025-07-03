# (Q)1. Write a function for arithmetic operators(+,-,*,/)
#Answr

'arithmetic operators'
a=50
b=20

print (a+b)   #addition
print (a-b)  #Subtraction
print (a*b) # Multiplication
print (a/b)  #Division


# (Q.2)  Write a method for increment and decrement operators(++, --)
#answr

def increment_decrement(value):
    print("Original value:", value)

    # Increment
    value += 4
    print("After increment:", value)

    # Decrement
    value -= 5
    print("After decrement:", value)


#  Using this method
increment_decrement(8)


#(Q.3)  Write a program to find the two numbers equal or not.
#answr

# Input two numbers for this  user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the numbers are equal
if num1 == num2:
    print("The two numbers are equal.")
else:
    print("The two numbers are not equal.")

# (Q.4) Program for relational operators (<,<==, >, >==)
# answr

# Input any two numbers using this
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using the relational operators to compare the numbers
print(f"{num1} < {num2} : {num1 < num2}")
print(f"{num1} <= {num2} : {num1 <= num2}")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} >= {num2} : {num1 >= num2}")


#(Q.5) Print the smaller and larger number
# answr
' show using this  min() and max() functions'

# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find smaller and larger numbers
smaller = min(num1, num2)
larger = max(num1, num2)

print(f"Smaller number: {smaller}")
print(f"Larger number: {larger}")
