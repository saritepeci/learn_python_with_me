# Cheat Sheet: Python Basics
# Variables and Data Types
# In Python, you can create variables to store data. Python is a dynamically typed language,    which means you don't need to declare the type of a variable. The type is inferred from the value you assign to it. Here are some common data types in Python:
# String: A sequence of characters enclosed in quotes. For example:
name = "John"
# Integer: A whole number without a decimal point. For example:
age = 30
# Float: A number with a decimal point. For example:
height = 5.9
# Boolean: A value that can be either True or False. For example:
is_student = True
# List: An ordered collection of items that can be of different types. For example:
fruits = ["apple", "banana", "cherry"]
# Tuple: An ordered collection of items that cannot be changed (immutable). For example:
coordinates = (10, 20)
# Dictionary: A collection of key-value pairs. For example:
person = {"name": "John", "age": 30, "height": 5.9}
# Set: An unordered collection of unique items. For example:
unique_numbers = {1, 2, 3, 4, 5}
# You can also use the type() function to check the type of a variable. For example
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>  
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>
print(type(fruits))  # Output: <class 'list'>
print(type(coordinates))  # Output: <class 'tuple'>
print(type(person))  # Output: <class 'dict'>
print(type(unique_numbers))  # Output: <class 'set'>

# String Methods
# lower(): Converts all characters in a string to lowercase. For example:
print(name.lower())  # Output: "john"
# upper(): Converts all characters in a string to uppercase. For example:
print(name.upper())  # Output: "JOHN"

# strip(): Removes any leading and trailing whitespace from a string. For example:
greeting = "   Hello, World!   "
print(greeting.strip())  # Output: "Hello, World!"
# split(): Splits a string into a list of substrings based on a specified delimiter. For example:
sentence = "Hello, how are you?"
print(sentence.split())  # Output: ["Hello,", "how", "are", "you?"]

# replace(): Replaces occurrences of a specified substring with another substring. For example:
print(name.replace("o", "a"))  # Output: "Jahn"

# find(): Returns the index of the first occurrence of a specified substring. For example:
print(name.find("o"))  # Output: 1

# count(): Returns the number of occurrences of a specified substring. For example: 
print(name.count("o"))  # Output: 1

# isalpha(): Returns True if all characters in the string are alphabetic. For example:
print(name.isalpha())  # Output: True

# isdigit(): Returns True if all characters in the string are digits. For example:
print(name.isdigit())  # Output: False

# isspace(): Returns True if all characters in the string are whitespace. For example:
print(name.isspace())  # Output: False

# == Comparison Operators
print("pass to false\n")
age = 25 
age == 30
print(age == 30)  # Output: False

# for loop
for num in range(1, 10): 
    print(num) # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

fruits = ["apple", "banana", "orange", "grape", "kiwi"] 
for fruit in fruits:
    print(fruit) # Output: "apple", "banana", "orange", "grape", "kiwi"


class Points(object):
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def print_point(self): 
        print('x=', self.x, ' y=', self.y) 
p1 = Points("A", "B") 
p1.print_point()  # Output: x= A  y= B