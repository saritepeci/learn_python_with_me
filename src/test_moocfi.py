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

# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == previous_word:
#         break
#     story += word + " "
#     previous_word = word

# print(story.strip())


# x = int(input("Upper limit: "))
# y = int(input("Base: "))
# i = 1
# while i <= x:
#     print(i)
#     i = i * y


###############
#failed
# def greet(hash:int):
#     line = (hash, '#')
#     print(line)

# def square_of_hashes(times):
#     return greet(times)
        

# square_of_hashes(5)
# print()
# square_of_hashes(3)

###############
'''
Index: 0
New value: 10
[10, 2, 3, 4, 5]
Index: 2
New value: 250
[10, 2, 250, 4, 5]
Index: 4
New value: -45
[10, 2, 250, 4, -45]
Index: -1
'''

# l= [1, 2, 3, 4, 5]
# while True:
#     indx = int(input("Index: "))
#     if indx ==-1:
#         break
#     val = int(input("New value: "))
#     l[indx] = val
#     print(l)

############
import numpy as np

A = np.array([[0,1,1],[1,0,1]])
B = np.array([[1,1],[1,1],[-1,1]])
C = np.dot(A,B);

print(C)
#print(np.ndim())