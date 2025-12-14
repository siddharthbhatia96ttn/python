#Define a function calculate_area that calculates the area of a rectangle and return the result. If no width is provided, it defaults to 10.
def calculate_area(length, width=10):
    return length * width

print(calculate_area(5))      
print(calculate_area(5, 4))   


# Write a recursive function to compute the factorial of a non-negative integer.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Example
print(factorial(5))

# Write a function that takes one parameter as a string and reverse it and return.
def reverse_string(s):
    reverse = ""
    for ch in s:
        reverse = ch + reverse
    return reverse

print(reverse_string("hello"))

# Write a Python function that takes two parameters as lists and to sum all the numbers in a list. 
def sum_two_lists(list1, list2):
    total = 0
    for num in list1:
        total += num
    for num in list2:
        total += num
    return total


a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]

print(sum_two_lists(a, b))

# Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list
def distinct_sorted_list(lst):
    return sorted(set(lst))


a = [4, 1, 2, 3, 3, 1, 3, 4, 5, 1, 7]

print(distinct_sorted_list(a))
