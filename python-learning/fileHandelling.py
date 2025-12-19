#Write a Python program to read the entire content of a file named sample.txt and display it.
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'sample.txt' does not exist.")

#Write a Python program to count the number of words in a file named words.txt
try:
    with open("words.txt", "r") as file:
        content = file.read()
        words = content.split()
        print("Number of words:", len(words))
except FileNotFoundError:
    print("The file 'words.txt' does not exist.")


#Create a program to write the string “Hello, Python!” into a file named output.txt.
import csv
students = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", 1, 85],
    ["Bob", 2, 90],
    ["Charlie", 3, 78]
]

with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("students.csv file created successfully.")


#From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.

def read_file_generator(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

for line in read_file_generator("sample.txt"):
    print(line)