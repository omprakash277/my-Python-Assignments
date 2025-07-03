#Q.1 Different ways creating a string
#answr
s1 = 'Hello'
s2 = "World"
s3 = '''Multiline
String'''
num = 10
s4 = str(num)
s5 = 'Value: {}'.format(num)
s6 = f'Value plus 5: {num + 5}'
s7 = 'Number: %d' % num

print(s1, s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

#Q.2  Concatenating two strings using + operator
#answr
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# Q.3  Finding the length of the string
#answr
my_string = "Hello, world!"
length = len(my_string)
print("Length of the string:", length)

# Q.4 Extract a string using Substring
#answr
# Original string
text = "Hello, Python!"

# Extract substring from index 7 to 12
substring = text[7:12]

print(substring)


#Q.5 Searching in strings using index()
#answr
text = "Hello, welcome to my world."

# Find index of substring "welcome"
position = text.index("welcome")
print("Position of 'welcome':", position)

# Find index of substring "o" starting from index 5
position_o = text.index("o", 5)
print("Position of 'o' after index 5:", position_o)

# Q.6 Matching a String Against a Regular Expression With matches()
#answr
import re

pattern = r'foo'   # regex pattern to match
string = 'foo bar' # string to test

match = re.match(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")


#Q.7 Comparing strings
#answr
def compare_strings(str1, str2):
    if str1 == str2:
        print("Strings match!")
    else:
        print("Strings do not match.")

# Example usage
string1 = "HelloWorld"
string2 = "HelloWorld"
string3 = "helloworld"

compare_strings(string1, string2)
compare_strings(string1, string3)

# Q.8  startsWith(), endsWith() and compareTo()
#answr

#1. startsWith()
text = "OM, welcome to OM."

# Check if string starts with "OM"
if text.startswith("OM"):
    print("The string starts with 'OM'")
else:
    print("The string does not start with 'OM'")

#2 endsWith()
text = "OM, welcome to Tutorialspoint."

# Check if string ends with "SAHU."
if text.endswith("SAHU."):
    print("The string ends with 'SAHU.'")
else:
    print("The string does not end with 'SAHU.'")

#3 compareTo()
def compare_to(str1, str2):
    if str1 == str2:
        return 0
    elif str1 < str2:
        return -1
    else:
        return 1

# Compar "normal bike" and "super bike"
result = compare_to("normal bike", "super bike")

if result == 0:
    print('"normal bike" is equal to "super bike"')
elif result < 0:
    print('"normal bike" less than "super bike"')
else:
    print('"normal bike" greater than "super bike"')

#Q.9 Trimming strings with strip()
#answr
# Example string with leading and trailing spaces
message = ' HELLO OM  '

# trailing whitespaces
trimmed_message = message.strip()

print('Original:', repr(message))
print('Trimmed:', repr(trimmed_message))

#Q.10  Replacing characters in strings with replace()
#answr
# Original string
text = "I like CD GAMES"

# Replace "CD GAMES" with "MOBILE GAMES"
new_text = text.replace("CD GAMES", "MOBILE GAMES")

print(new_text)

#Q.11 Splitting strings with split()
#answr
text = "apple,banana,grape,orange"
# Split the string by comma
fruits = text.split(",")
print(fruits)
limited_split = text.split(",", 2)
print(limited_split)

#Q.12 Converting integer objects to Strings
#answr
number = 21
string_number = str(number)
print(string_number)
print(type(string_number))

#Q.13 Converting to uppercase and lowercase
#answr
text = "OM PRAKASH SAHU "
print(text.upper())  # Convert to uppercase
print(text.lower())  # Convert to lowercase
