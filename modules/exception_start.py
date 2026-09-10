
#x= 10 / 0
#print(x)

#Exception handling

# try:
#     x= 10 / 0
# except:
#     print("Well that didn't work")

try:
    answer = input("What should I divide 10 by")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("you can not")
except ValueError as e:
    print("no nooo")
    print(e)
finally:
    print("You always runs")

