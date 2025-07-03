# (Q.1) Write a program to print your name. #
#ANSWR
# This program prints a name
print("Omprakash Sahu")


# (Q.2) Write a program for a Single line comment and multi-line comments #
#ANSWR
#  Single line comment

#(#)This sympoble using Single line Comment
# print("Omprakash Sahu")


# multi-line comments

"""
This is another type of multi-line comment
using triple double quotes.
"""


# (Q.3 )Define variables for different Data Types int, Boolean, char, float, double and print on the
#ANSWR
#1. Data Types (int)

# Step 1: Declare the  integer variable
int = 10

# Step 2: it is Print the integer value
print("Integer value:", int)

# Step 3: Checks and print the data type of the variable
print("Type of variable:", type(int))


#2. Data Types (Boolean)
# Step 1: Fast theny declare Boolean variable in  Ram and Shyam
ram = True      #  Ram is available
shyam = False   # Shyam is not available

# Step 2: Print their Boolean values
print("Is Ram available?", ram)
print("Is Shyam available?", shyam)

# Step 3: Print the data types  they are Boolean
print("Type of ram:", type(ram))
print("Type of shyam:", type(shyam))


#3. Data Types (char)
#ANSWR

# Step 1: Declare variables  single characters
letter = 'A'        # a letter
digit = '7'         # a digit as a character
symbol = '@'        # a symbol

# Step 2: Print the characters
print("Letter:", letter)
print("Digit:", digit)
print("Symbol:", symbol)

# Step 3:  the type of one variable to confirm it's a string
print("Type of letter:", type(letter))



#4. Data Types (float)
#ANSWR

# Step 1: Declare float variables
my_float = 8.12
my_negative_float = -0.9

# Step 2: Print the float values
print("Float value:", my_float)
print("Negative float value:", my_negative_float)

# Step 3: Convert other types to float
int_value = 15
string_value = "42.5"

float_from_int = float(int_value)
float_from_string = float(string_value)

print("Float from int:", float_from_int)
print("Float from string:", float_from_string)

# Step 4: Check the Data type  float variable
print("Type of my_float:", type(my_float))


#5. Data Types (double)
# Step 1: Declare the  double precision float variable
my_double = 4.141

# Step 2: Print the value
print("Double precision value:", my_double)

# Step 3: Perform arithmetic operations
add_result = my_double + 5.5
mul_result = my_double * 6

print("Addition result:", add_result)
print("Multiplication result:", mul_result)

# Step 4: Show type of
print("Type of my_double:", type(my_double))

# (Q.4 )4. Define the local and Global variables with the same name and print both variables and
#understand the scope of the variables
 #ANSWR

x = "global variable"  # The Global variable

def my_function():
    x = "local variable"  # Local variable with the same name
    print("Inside function:", x)  # Prints local variable

my_function()
print("Outside function:", x)  # Prints global variable
