album_ratings =[10.0,5.6,6.5,8.0,9.5,7.0,8.5,9.0,6.0,7.5]

#sum of ratings
sum_album_ratings = sum(album_ratings)
print(f"Sum of album ratings: {sum_album_ratings}")

# Calculate the average rating
average_album_rating = sum_album_ratings / len(album_ratings)
print(f"Average album rating: {average_album_rating}")

#sort ratings
sorted_album_ratings = sorted(album_ratings)
print(f"Sorted album ratings: {sorted_album_ratings}")

album_ratings.sort()
print(f"Album ratings after in-place sort: {album_ratings}") # Note: album_ratings is now sorted in-place

####----------------------------------------####

# Functional programming tools: map, filter, reduce, partial, lru_cache, sorted with key, and function composition.
def add1(a):
    b=a+1
    return b

c = add1(5)
print(c)  # Output: 6

d=add1(8)
print(d)  # Output: 9


def Mult(a,b):
    c=a*b
    return c

e=Mult(5,6)
print(e)  # Output: 30

e=Mult(2,"michael jackson ")
print(e)  # Output: "michael jackson michael jackson "

e=Mult('michael jackson',2)
print(e)  # Output: "michael jackson michael jackson "

def MJ():
    print('Michael Jackson is the King of Pop!')

def NoWork():
    pass
    return None
print(NoWork())  # Output: None


def Square(a):
    b= a*a
    print(b," is the square of ",a)
    return b

Square(5)  # Output: 25  is the square of  5

#Using loops in functions
def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album", i ,"Rating is: ", s)
album_ratings =[10.0,5.6,6.5,8.0,9.5,7.0,8.5,9.0,6.0,7.5]

album_ratings.sort()
printStuff(album_ratings)

#Collecting arguments in a function
def ArtistNames(*names):
    for name in names:
        print(name)

ArtistNames("Michael Jackson", "Madonna", "Prince")

print("Scope and global variables demonstration:")
#Scope and global variables
def AddDC(x):
    x = x + "DC"
    print(x)
    return x

x = "AC"
z = AddDC(x)  # Output: "ACDC"

def PinkFloyd():
    global ClaimedSales
    ClaimedSales = "45 Million"
    return ClaimedSales

PinkFloyd()  # Output: "45 Million"
print(ClaimedSales)  # Output: "45 Million"

print("End of scope and global variables demonstration.")

# Using functions as arguments
def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c']) # Output: a1, b1, c1

#sorted again :))
L=[1,3,2]

sorted(L) # Output: [1, 2, 3] - sorted returns a new sorted list
print(L) # Output: [1, 3, 2] - original list remains unchanged