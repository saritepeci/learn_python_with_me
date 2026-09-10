import os
from os import path
import shutil
from zipfile import ZipFile

if path.exists("file_text_start.txt"):
    src = path.realpath("file_text_start.txt")

    dst = src + ".bak"
    shutil.copy(src, dst)

    #os.rename("file_text_start.txt", "new_file_text_start.txt")

else:
    print("File does not exist")


with ZipFile("file_text_start_1.zip", "w") as newzip:
    newzip.write("file_text_start.txt")
    newzip.write("file_text_start.txt.bak")


