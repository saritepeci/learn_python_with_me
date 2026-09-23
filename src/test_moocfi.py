'''Part 1
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl

Part 2
Change the program so that the loop ends also if the user types in the same word twice in a row.
Please type in a word: dark
Please type in a word: and
Please type in a word: stormy
Please type in a word: night
Please type in a word: night
It was a dark and stormy night
'''

story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous_word:
        break
    story += word + " "
    previous_word = word

print(story.strip())



x = int(input("Upper limit: "))
y = int(input("Base: "))
i = 1
while i <= x:
    print(i)
    i = i * y
