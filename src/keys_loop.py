for number in range(1, 4):
    print(number)

print("Now first number not included:")
    
for number in range(4):
    print(number)


print("Now counting backwards:")
for number in range(5, 0, -1):
    print(number)

# enumerate() gives both index and value when iterating over a sequence
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

# other example of enumerate
# Loop through the list and iterate on both index and element value
print("Now with enumerate:")

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# len with loops
# For loop example

dates = [1982,1980,1973]
N = len(dates)

print(len(dates))  # 3

for i in range(N):
    print(dates[i]) 

#Using break and continue
print("Using break and continue:")

count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)