import pprint

# regular assigment statement assign a value
x=5
print(x)

# the assigment operator is part of an expression
(x := 10)
print(x)

# The assigment expression is useful for writing concide code
'''
thestr = str(input("Value? "))
while (thestr := str(input("Value? "))) != "exit":
    print(thestr)
    thestr = str(input("Value? "))
    '''

#Short format with (thestr := str(input("Value? ")))
while (thestr := str(input("Value? "))) != "exit":
    print(thestr)