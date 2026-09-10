import os
from os import path


print(os.name) # nt == Windows pc

print("Item exists:", path.exists("file_text_start.txt")) #os.path.exists("file_text_start.txt")
print("Item is a file:", path.isfile("file_text_start.txt"))
print("Item is a directory:", path.isdir("file_text_start.txt"))

print("Item is path:", path.realpath("file_text_start.txt"))
print("Item is path:", path.split(path.realpath("file_text_start.txt")))

# get modify time


