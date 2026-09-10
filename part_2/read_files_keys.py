#read mode
file_keys = open("file_text_start.txt", "r")

if file_keys.mode == 'r':
    content = file_keys.readlines()
    for line in content:
        print(line)

    #print(content)

#Close line
#file_keys.close()

