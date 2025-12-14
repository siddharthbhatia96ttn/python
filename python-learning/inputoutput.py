#Task: Write a program that asks the user for their name and then prints a greeting   message using their name.
name=input("enter you name: ")
print("Welcome ",name)

#Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
sign = input("Enter sign for calculation (+, -, *, /): ")

if sign == "+":
    result = num1 + num2
    print("Added value is:", result)

elif sign == "-":
    result = num1 - num2
    print("Subtracted value is:", result)

elif sign == "*":
    result = num1 * num2
    print("Multiplied value is:", result)

elif sign == "/":
    if num2 != 0:
        result = num1 / num2
        print("Divided value is:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operator")


#Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names = input("Enter names separated by commas: ")
name_list = names.split(",")
print("List of names:", name_list)


#Task: Ask the user to enter their age and check if they are eligible to vote based on their age.

age=int(input("Enter your age: "))
if age>=18:
 print("You are elgible for vote")
else:
 print("You are  not elgible for vote")



#Task: For value = 3.14159, Using f-string print output for only up to 2 decimal places.
value=float(input("Enter value in points"))
print(f"{value:.2f}")