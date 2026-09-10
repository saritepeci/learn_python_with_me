
x, y = 12, 145
#
if x < y:
    print(f"x is less than y: x:{x}, y:{y}")
elif x == y:
    print("x is same as y")
else:
     print("x is king")
#
result = "x is less than y" if(x<y) else "x is king"
print (result)


###Loops

# x = 0
# while x<5:
#     #print(x)
#     x +=1

days= ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# for d in days:
#     if(d=="Fri"):
#         continue
#     elif(d=="Sun"):
#         break
#     print(d)

for i, d in enumerate(days):
    print(i, d)