#open and write
# file_keys = open("file_text_start.txt", "w+")
# file_keys.write("This is test files")
# file_keys.close()

#append
file_keys = open("file_text_start.txt", "a+")
file_keys.write("This is test files, more information.")
file_keys.write("\n second line \nllllllllllll.")

#Close line
file_keys.close()





