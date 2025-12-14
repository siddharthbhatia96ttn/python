# Convert 3.75 to integer
a = int(3.75)
print("Converted values is",a)

# Convert "123" to float
b = float("123")
print("Float value is",b)

# Convert 0 to boolean
c = bool(0)
print("Boolean converted value is",c)

# Convert False to string
d = str(False)
print("False to string value",d)

print("------------")

# 2. Convert string to uppercase
x = "hello"
print("Upper case converted value is",x.upper())

print("------------")

# 3. Addition and type checking
x = 5
y = 3.14

z = x + y
print("Added value is",z)
print("Data type is",type(z))

# Convert z to integer
z_int = int(z)
print("Integer value is",z_int)

print("------------")

# 4. String operations
s = "hello"

# Convert to uppercase
print("Upper case value is",s.upper())

# Replace 'e' with 'a'
print("Replaced value is",s.replace('e', 'a'))

# Check if string starts with 'he'
print(s.startswith('he'))

# Check if string ends with 'lo'
print(s.endswith('lo'))
