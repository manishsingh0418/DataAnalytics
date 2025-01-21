a = "Harry Potter and the Goblet of Fire"
print(a)

# to find the length of the string
print(len(a))

# to find the number of times a character is occuring

print(a.count("o"))

# to convert each letter into upper case
print(a.upper())

# to convert each letter into lower case
print(a.lower())

# to find the index of any character
print (a.index("o",15,34))

# to convert the first letter to capital
print(a.capitalize())

# to convert sting into lower case
print(a.casefold())

# to write variable inside a string

name="John"
age= 24
b="my name is {} . and my age is {}"
print(b.format(name,age))

# it fills the given characters and centralizes a string
print(name.center(20,"*"))