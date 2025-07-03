#Q.1 Write a program to print  “Bright IT Career”  ten times using for loop
#answr

for i in range(10):
    print("Bright IT Career")

#(Q.2) Write a java program to print 1 to 20 numbers using the while loop.
#answr
#  the starting number
num = 1

# Loop is greater than 20
while num <= 20:
    print(num)
    num += 1  # increment the number 1 by 1


#(Q.3) Program to equal operator and not equal operators
#answr
# Input two values number for user
val1 = input("Enter first value : ")
val2 = input("Enter second value : ")

# Check if the values are equal
if val1 == val2:
    print("two values are equal.")
else:
    print(" two values are not equal.")

# Demonstrate not equal operator
if val1 != val2:
    print("Using '!=' operator: The values are different.")
else:
    print("Using '!=' operator: The values are the same.")



#Q.4 Write a program to print the odd and even numbers.
#answr
# Define the range
start = 1
end = 20

print("Even numbers:")
for num in range(start, end + 1):
    if num % 2 == 0:  # The check if number is even
        print(num, end=' ')

print("\nOdd numbers:")
for num in range(start, end + 1):
    if num % 2 != 0:  # The check if number isodd
        print(num, end=' ')

#(Q.5) Write a program to print largest number among three numbers.
#answr
# Input three numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Determine the largest number
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)


# Q.6 Write a  program to print even number between 10 and 20 using while
#answr
num = 10  # start from 10

while num <= 20:
    if num % 1 == 0:  # The Check if the number is even
        print(num)
    num += 5 # Increment the number  5


# Q.7 Write a program to print 1 to 10 using the do-while loop statement.
#answr
num = 1 # start from 1

while True:
    print(num)
    num += 1
    if num > 10:
         break


#Q.8 Write a program to find Armstrong number or not
#answr
def is_armstrong(num):
    # Convert the number to a string to find  number of digits
    num_str = str(num)
    n = len(num_str)

    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** n  # Raise each digit to the power n and add

    return sum_of_powers == num

# Input from the user
number = int(input("Enter a number: "))

# Check and print result
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# Q.9 rite a program to find the prime or not.
#answr
# Input number for user
num = int(input("Enter a number: "))

# Prime numbers are greater than 2
if num <= 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 2):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


#Q.10 . Write a program to palindrome or not.
#answr
# Input string from the user
o = input("Enter a string: ")

# Convert string to lowercase for case-insensitive comparison
o = o.casefold()

# Reverse the string
rev_s = o[::-1]

# Check if the original string is equal to its reverse
if o == rev_s:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Q.11  Program to check whether a number is EVEN or ODD using switch
#answr
# Input number from the user
num = int(input("Enter a number: "))

# Use match-case to check even or odd
match num % 2:
    case 0:
        print(f"{num} is Even.")
    case 1:
        print(f"{num} is Odd.")

# Q.12  Print gender (Male/Female) program according to given M/F using switch
#answr
gender_input = input("Enter gender (M/F): ").upper()  # Convert to uppercase

match gender_input:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Soory Invalid input")
