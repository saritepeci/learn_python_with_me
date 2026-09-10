
"""
open() function is used to open a file in Python. It takes two parameters: the name of the file and the mode in which the file is opened. 
The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'x' for creating a new file.
In this example, we will read the contents of a file named "file1.txt" using the open() function.
"""
from os import write


file1= open("C:/development/learn_python/src/file1.txt", "r")
file1.mode 
'r'
print(file1.read())

file1.close()

# other options for opening a file with open() function

with open("C:/development/learn_python/src/file1.txt", "r") as file1:
    file_stuff = file1.read()
    print("Before closing the file, the contents were:", file_stuff)
    file_stuff = file1.readline()
    print("After reading the first line, the contents were:", file_stuff)
print(file1.closed)
print("After closed the file, the contents were:", file_stuff)


#creating a new file and writing to it
with open("C:/development/learn_python/src/file3.txt", "w") as file3:
    file3.write("After created (x) to run with (w), the contents were: ")
    file3.write("\n")
    print(file3.closed)

with open("C:/development/learn_python/src/file2.txt", "r") as file2:
    file2_stuff = file2.read()
    print("After writing to the file, the contents were:", file2_stuff)
    print(file2.closed)


#In Python, you can use the 'a' mode when opening a file to append new data to an existing file without overwriting its contents.
with open("C:/development/learn_python/src/file4.txt", "a") as file4:
    with open("C:/development/learn_python/src/file3.txt", "r") as readfile:
        for line in readfile:
            file4.write(line)
    print(file4.closed)



# The name attribute retrieves the file's title
# print(file1.name)

