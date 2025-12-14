#Task Write a program that takes the input from the user and checks if a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”
strings = ["civic", "hello"]

for s in strings:
    reverse = ""
    for ch in s:
        reverse = ch + reverse

    if s == reverse:
        print(s, "is a Palindrome")
    else:
        print(s, "is NOT a Palindrome")
#Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
n = int(input("Enter number of terms: "))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Print all even numbers between 1 and 20 using a while loop.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#Find the first occurrence of a number in a list and stop further searching. 
numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if num == search_for:
        print("Found:", num)
        break

#Using continue statement, print only the odd numbers from 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


#Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.
day = input("Enter day: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")