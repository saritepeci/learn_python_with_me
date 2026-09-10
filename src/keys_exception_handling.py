"""
"Please enter your name: " # This is a string literal, not an expression.
"""
from webbrowser import get

try:
    get_value = lambda d, k: d[k]  # A simple function to get a value from a dict by key.
    my_dict = {"a": 1, "b": 2}
    print(get_value(my_dict, "a"))  # This will print 1.
    print(get_value(my_dict, "c"))  # This will raise a KeyError.
except KeyError as e:
    print(f"KeyError: {e}")
    print("The key you are trying to access does not exist in the dictionary.")
else:
    print("Value retrieved successfully.")


my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
#missing = my_list[5]  # Raises IndexError


my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
#missing = my_dict["city"]  # Raises KeyError

#Attempting to divide by zero
# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")

#If the user enters the value of `b’ as 0, what is expected as the output?
a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a =", a)
except:
    print("There was an error")

# Dividing by zero will raise a ZeroDivisionError, which will be caught by the except block, resulting in the output "There was an error".
# Dividing nonnumeric input will raise a ValueError, which will also be caught by the except block, resulting in the same output "There was an error".


