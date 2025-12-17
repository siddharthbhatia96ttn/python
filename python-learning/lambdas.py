#Given a list let's see how to double each element of the given list. Using map() 
a = [1, 2, 3, 4]
result=[]
for x in a:
    result.append(x*2)

print(result)    


#Use filter() and lambda to extract all even numbers from a list of integers.
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data=[]

data = list(filter(lambda x: x % 2 == 0, b))

print(data)

#Use reduce() and lambda to find the longest word in a list of strings.
words = ["apple", "banana", "cherry", "date"]

longest_word = max(words, key=len)
print(longest_word)


#Use filter() to select names with 7 or fewer characters from the list.
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

result = list(map(lambda x: round(x * x, 1), my_floats))

print(result)

#Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

