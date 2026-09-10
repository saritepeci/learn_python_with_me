# def func_simple():
#     name = input("Your name? ")
#     print("Hi", name)

# def hello_func(greeting):
#     print(greeting)
#     name = input("Name? ")
#     print(greeting)

# hello_func("Hi")
# hello_func("ok ok enough")


# def cube(x):
#     return x*x*x

# result=cube(2.22)
# print(result)



# def func_new(greeting, name=None):
#     print("Hi")
#     if name== None:
#         name = input("Who are you! ")
#     print(greeting, name)
# func_new("Heyyyy")


def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#print(multi_add(10,2,5,3,1,6,7,8,4))


numbers =[7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

