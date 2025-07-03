# Q.1  Write a function to add integer values of an array
#answr

def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example for usage
arr = [4, 3, 63, 21]
result = sum_of_array(arr)
print("Sum of the array is:", result)


#Q.2 Write a function to calculate the average value of an array of integers
#Answr
def find_average(arr):
    if len(arr) == 0:
        return 0  # Handle empty array case to avoid division by zero
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum / len(arr)

# Example usage
arr = [78, 21, 87, 90, 74]
print("Average of array elements:", find_average(arr))

#Q.3 Write a program to find the index of an array element
#answr
# Sample array (list)
arr = [100, 200, 300, 400, 500]

# Element to find
element = 400

try:
    idx = arr.index(element)
    print(f"The index of {element} is: {idx}")
except ValueError:
    print(f"{element} is not found in the array.")

#Q.4 Write a function to test if array contains a specific value
#answr
def contains_value(arr, value):
    return value in arr

# Example usage
my_array = [10, 20, 30, 40, 50]
print(contains_value(my_array, 10))  # Output: True
print(contains_value(my_array, 600))  # Output: False

# Q.5  Write a function to remove a specific element from an array answr def remove_element(arr, element):
  #answr

# Define the function to remove an element from a list
def remove_element(arr, element):
    try:
        arr.remove(element)
        print(f"{element} has been removed from the list.")
    except ValueError:
        print(f"{element} not found in the list.")

# Example usage
my_list = [10, 20, 30, 80, 40, 50]
remove_element(my_list, 20)
print("Updated list:", my_list)

#Q.6 Write a function to copy an array to another array
#answr
def copy_array(arr):
    # Using list slicing (produces a shallow copy)
    copied_arr = arr[:]
    return copied_arr

# Example usage
original_array = [145, 201, 453, 754, 125]
copied_array = copy_array(original_array)

print("Original array:", original_array)
print("Copied array:", copied_array)

# Q.7 Write a function to insert an element at a specific position in the array
#answr
def insert_element(arr, element, position):
    if position < 0 or position > len(arr):
        print("Error: Position out of bounds.")
        return arr
    arr.insert(position, element)
    return arr

# Example usage:
my_array = [10, 20, 30, 40, 50]
print("Original array:", my_array)

# Insert 87 at index 3
updated_array = insert_element(my_array, 87, 3)
print("Array after insertion:", updated_array)

#(Q.8)Write a function to find the minimum and maximum value of an array
#answr
def find_min_max(arr):
    if not arr:
        return None, None  # Handle empty list case
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# Example usage
numbers = [152, 85, 87, 70, 47]
min_val, max_val = find_min_max(numbers)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")


#(Q.9) Write a function to reverse an array of integer values
#answr
def reverse_array(arr):
    return list(reversed(arr))

# Example
array = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(array))

#(Q.10) . Write a function to find the duplicate values of an array
#answr
def find_duplicates(arr):
    return list(set([x for x in arr if arr.count(x) > 1]))

# Example usage:
my_array = [1, 2, 3, 1, 2, 4, 5, 6, 5]
print(find_duplicates(my_array))


#(Q.11) Write a program to find the common values between two arrays
#answr
def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage
array1 = [3, 1, 5, 4, 2, 5]
array2 = [8, 4, 5, 7, 4, 6]

common_elements = find_common_elements(array1, array2)
print("Common elements:", common_elements)

#(Q.12) Write a method to remove duplicate elements from an array
#answr
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))

#(Q.13 & 14)  Write a method to find the second largest number in an array
#answr
def second_largest(arr):
    max1 = float('-inf')
    max2 = float('-inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num
    return max2 if max2 != float('-inf') else None

# Example usage:
arr = [12, 35, 1, 10, 34, 1]
print("Second largest number is:", second_largest(arr))


# Q.15  Write a method to find number of even number and odd numbers in an array
#answr
def count_even_odd(arr):
    count_even = 0
    count_odd = 0
    for num in arr:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

# Example usage
numbers = [1, 2, 3, 5, 7, 8, 9, 10]
even_count, odd_count = count_even_odd(numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

#Q.16 Write a function to get the difference of largest and smallest value
#answr
def difference_max_min(arr):
    if not arr:
        return None  # Handle empty array
    return max(arr) - min(arr)

# Example usage
numbers = [10, 4, 2, 8, 6]
print("Difference between largest and smallest:", difference_max_min(numbers))

#Q.17 Write a method to verify if the array contains two specified elements(12,23)
#answr
def contains_both(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# Example usage
array = [5, 12, 7, 23, 9]
print(contains_both(array, 12, 23))  # Output: True

array2 = [5, 12, 7, 9]
print(contains_both(array2, 12, 23))  # Output: False

#Q.18  Write a program to remove the duplicate elements and return the new array
#answr
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))
