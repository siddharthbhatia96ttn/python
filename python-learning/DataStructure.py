#Task Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]

print("Maximum value:", max(nums))
print("Minimum value:", min(nums))

#Task Given two lists below, merge the values from both lists to one and print
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = a + b
print(c)

#Task From a list, print the number of times the value 3 appears in the list:
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]

count = a.count(3)
print("Number of times 3 appears:", count)

#Task From below list, Sort the list and print
a = [1, 3, 4, 5, 2, 1, 3, 9, 3]

a.sort()
print(a)

#Task Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}

numbers.add(6)

print(numbers)

#Task Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}

numbers.remove(3)

print(numbers)

#Task Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)

# Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')

count = fruits.count('apple')
print("Number of occurrences of 'apple':", count)

 #Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)


# Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person["age"])

#Add new key,  gender to dictionary and assign “M” to it and print
person = {"name": "Alice", "age": 30, "city": "New York"}

person["gender"] = "M"

print(person)

#Remove the key "city" from the above Dict and print
person = {"name": "Alice", "age": 30, "city": "New York", "gender": "M"}

del person["city"]

print(person)

#Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)
