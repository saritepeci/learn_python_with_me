def output_sum(first,second):
    print(first + second)

output_sum(1, 3)

def shout(message):
    message += "!!!!!"
    print(message)

shout("Yeah")

# len function
name ="Peter Pan"
lenght = len(name)
print(lenght)

def multiply(first,second):
    return first * second # return is better not print 

print(multiply(10, 20) + multiply(5, 2))

def add_one(num):
    return num +1 # if you use print output error

number = add_one(add_one(add_one(1)))
print(number)


def fac(n: int)-> float:
    print(n)
fac(3.3333)


def return_value(first: int, second: int):
    if first > second:
        return first
    else:
        print("second is big")
f = 10
s = 5
print(return_value(f, s)) # If second number big output: second is big and None Because without return !!!

def return_value_better_way(first: int, second: int):
    if first > second:
        return first
    else:
        return second