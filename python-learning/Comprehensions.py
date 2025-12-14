# Given a list of numeric strings, convert them into integers. Using List Comprehensions
strings = ["1", "2", "3", "4", "5"]

result = [int(s) for s in strings]
print(result)

# Extract all integers from a list that are greater than 10. Using List Comprehensions
numbers = [1, 5, 13, 4, 16, 7]

result = [n for n in numbers if n > 10]
print(result)

# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
squares = [i * i for i in range(1, 6)]
print(squares)

# Convert a 2D list into a 1D list.Using List Comprehensions
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]

flat_list = [num for row in matrix for num in row]
print(flat_list)


#Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
#Expected output : {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = {keys[i]: values[i] for i in range(len(keys))}
print(result)

#Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
	#Expected output : {'Alice': 85, 'Charlie': 90}
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}

result = {name: score for name, score in scores.items() if score > 80}
print(result)
