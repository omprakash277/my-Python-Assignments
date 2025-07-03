#Q.1 Create a Dictionary with at least 5 key value pairs of the Student ID and Name
#answr
# Creating a dictionary with 5 Student ID and Name pairs
students = {
    1001: "Alice",
    1002: "Bob",
    1003: "Charlie",
    1004: "David",
    1005: "Eve"
}

print(students)

#Q.2 Adding the values in dictionary
#answr
# Example dictionary with numeric values
my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

# Calculate the sum of all values using sum() and values()
total = sum(my_dict.values())

print("Sum of all values:", total)


#Q.3  Updating the values in dictionary
#answr
# Initial dictionary with Student ID and Name
students = {
    1001: "Alice",
    1002: "Bob",
    1003: "Charlie",
    1004: "David",
    1005: "Eve"
}
# Method 1: Update value by key assignment
students[1003] = "Charles"

# Method 2: Update using update() method with another dictionary
students.update({1005: "Eva"})

print(students)

#Q.4 Accessing the value in dictionary
#answr
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}

# Access using key directly
print(students[102])         # Output: Bob

# Access using get() method
print(students.get(103))     # Output: Charlie

# Access with get() providing default if key not found
print(students.get(999, "Not Found"))  # Output: Not Found

#Q.5 Create a nested loop dictionary
#answr
nested_dict = {}
for i in range(3):             # Outer loop for outer keys
    inner_dict = {}
    for j in range(2):         # Inner loop for inner keys
        inner_dict[f'key{j}'] = i + j
    nested_dict[f'outer{i}'] = inner_dict

print(nested_dict)


# Q.6  Access the values of nested loop dictionary
#answr
# Example nested dictionary
nested_dict = {
    'outer1': {'inner1': 10, 'inner2': 20},
    'outer2': {'inner1': 30, 'inner2': 40},
    'outer3': {'inner1': 50, 'inner2': 60}
}

# Accessing values by chaining keys
print(nested_dict['outer1']['inner1'])  # Output: 10
print(nested_dict['outer2']['inner2'])  # Output: 40
print(nested_dict['outer3']['inner1'])  # Output: 50

#Q.7 Print the keys present in a particular dictionary
#answr
# Sample dictionary
student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eva"
}

# Print all keys
for key in student_dict.keys():
    print(key)

#Q.8 Delete a value from a dictionary
#answr
my_dict = {'a': 1, 'b': 2, 'c': 3}
del my_dict['b']            # Removes key 'b' and its value
print(my_dict)              # Output: {'a': 1, 'c': 3}

# Or using pop()
value = my_dict.pop('c', None)  # Removes key 'c' and returns its value
print(value)                   # Output: 3
print(my_dict)                 # Output: {'a': 1}
