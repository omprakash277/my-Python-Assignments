#Q.1 Write a program to generate Arithmetic Exception without exception handling
#answr
num = 10
den = 2
result = num / den  # This will raise ZeroDivisionError (Arithmetic Exception)
print(result)
#Q.2  Handle the Arithmetic exception using try-catch block
#answr

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Q.3 Write a program with multiple catch blocks
#answr
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter integers only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#Q.4 Write a program with finally block
#answr
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Executing the finally block.")

divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # Division by zero triggers exception

#Q.5 Write a program to generate Arithmetic Exception
#answr
num = 10
den = 4
result = num / den  # This will raise ZeroDivisionError (Arithmetic Exception)
print(result)

