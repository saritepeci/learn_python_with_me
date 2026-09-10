Set1 = {1, 2, 3, 4, 5}

print("Example of a set:", Set1)

Set1.add(6)
print("After adding an element to the set:", Set1) # Output: {1, 2, 3, 4, 5, 6}

Set1.add(6)
print("After trying to add a duplicate element to the set:", Set1) # Output: {1, 2, 3, 4, 5, 6} - no change since sets do not allow duplicates

Set1.update([7, 8, 9])
print("After adding multiple elements to the set:", Set1) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

Set1.remove(3)
print("After removing an element from the set:", Set1) # Output: {1, 2, 4, 5, 6, 7, 8, 9}

Set1.discard(10)  # No error if the element is not present
print("After discarding an element that is not in the set:", Set1) # Output: {1, 2, 4, 5, 6, 7, 8, 9} - no change since 10 was not in the set

Set1.pop()  # Removes and returns an arbitrary element from the set 
print("After popping an element from the set:", Set1) # Output: {2, 4, 5, 6, 7, 8, 9} - one element removed

# Check for membership in the set

"Who" in Set1  # Output: False - 'Who' is not in the set

5 in Set1  # Output: True - 5 is in the set


Set2 = {4, 5, 6, 7, 8, "k", "pop", 10.54}
print("Example of another set:", Set2)

# Find the union of two sets
union_set = Set1.union(Set2)
print("Union of Set1 and Set2:", union_set) # Output: {2, 4, 5, 6, 7, 8, 9, 'k', 'pop', 10.54}

# Check if superset
is_superset = Set1.issuperset(Set2)
print("Is Set1 a superset of Set2?", is_superset) # Output: False - Set1 does not contain all elements of Set2

# Check if subset
is_subset = Set1.issubset(Set2)
print("Is Set1 a subset of Set2?", is_subset) # Output: False - Set1 contains elements (like 2, 9) that are not in Set2


# Write your code below and press Shift+Enter to execute

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


album_set3 = album_set1.union(album_set2)
print("Union of album_set1 and album_set2:", album_set3) # Output: {'Thriller', 'AC/DC', 'Back in Black', 'The Dark Side of the Moon'}

is_subset = album_set1.issubset(album_set3)
print("Is album_set1 a subset of album_set3?", is_subset) # Output: True - album_set1 is a subset of album_set3 since all elements of album_set1 are in album_set3

{'a','b'} &{'a'} # Output: {'a'} - the intersection of the two sets is {'a'} since it is the only common element between them

