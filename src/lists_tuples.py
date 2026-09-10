import string
import os

ratings_paranteses = (10,9,6,5,10,8,9,6,2)

ratings_list = [4.5, 3.0, 5.0, 2.5, 4.0]

print("Ratings in parentheses:", ratings_paranteses)
print("Ratings in list:", ratings_list)

tupple_example = (1, ("pop","rock"), 3, 4, 5)
print(tupple_example[1][1])  # Output: rock

print("Example of a tuple:", tupple_example)

# Tuples are immutable; create a new tuple instead of modifying in place.
tupple_example = tupple_example + (6, 7, 8)
print("After concatenating values into a new tuple:", tupple_example)

# To "remove" an item, build a new tuple without that index.
tupple_example = tupple_example[1:]
print("After creating a new tuple without the first item:", tupple_example)

# To insert items, create a new tuple by slicing and concatenation.
tupple_example = tupple_example[:1] + (("jazz", "blues"),) + tupple_example[1:]
print("After creating a new tuple with inserted values:", tupple_example)


# Lists are mutable; you can modify them in place.

# Use extend to add elements to list
L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
print("After extending the list:", L)

# Use append to add elements to list
L.append(['top', 20.9])
print("After appending a list to the list:", L) 

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A) # Output: ['hard rock', 10, 1.2]

# Delete the element based on the index
del(A[2])
print('After change:', A) 

# Split the string, default is by space

A[0] = A[0].split()
print('After split:', A) # Output: [['hard', 'rock'], 10]

a_list = [1, "hello", [1,2,3], "True"]
print("Example of a list:", a_list)

#concatenating two lists
Anm = [1,2,3] + [1,1,1]
print("After concatenating two lists:", Anm)

Alalll=(1,2,3,4,5)
print(Alalll[1:4])

Bomnnn=[1,2,[3,'a'],[4,'b']]
print(Bomnnn[3][1]) # Output: 'b'

Ak = [1]
Ak.append([2, 3, 4, 5])
len(Ak) # Output: 2
print("Length of the list after appending a list:", len(Ak))

len(("disco",10,1.2, "hard rock",10)) # Output: 5