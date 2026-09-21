values = [1,2,3,4,4,5,6,7,8]

index = 0
while index < len(values):
    value = values[index]
    if value % 2 == 0:
        values.remove(value)
    else:
        index +=1

#print(values) # [1, 3, 5, 7]

############
# Wrong idea in buttom

# for val in values2:
#     if val %2 == 0:
#         values.remove(val)

# print(values) # [1, 3, 4, 5, 7]

############## Nested list
n =[[1,2,3], [6,5,4],[9,9,1]]
print(n)                     #[[1, 2, 3], [6, 5, 4], [9, 9, 1]]
print(len(n))                # 3

item = n[1][1]              # 5
print(item)

for row in n:
    for item in row:
        print(item)

print(n)

for row in range(len(n)):
    for item in range(len(n[row])):
        n[row][item] +=1

print(f"After range in for loop : {n}")

############ 
print("List_n in for loop or extern")
list_n = [1,2,3,4,5]

for val in list_n:
    val +=1
    print(val)

print(list_n)

############ enumerate

val_enum =[1,2,3,4,5,5,6,7,8,11,22,33,33,44,55,33,66]

for index,value in enumerate(val_enum):
    if value % 2 ==0:
        val_enum[index]=0

    #print(f"Index: {index}, value: {value}")

############ reference in python
print(" reference in python")
origin_list = [1, 2, 3, 4]

reference_list = origin_list
reference_list[0] = -1

print(origin_list)       # same output [-1, 2, 3, 4]
print(reference_list)    # same output [-1, 2, 3, 4]

############
def increase_first(m_list:list):
    m_list[0] = 100

l=[10,21,32,43]
increase_first(l)
print(l)
############ This example problamatic better way above:
def second_smallest_item_bad(l:list):
    l.sort()
    return l[1]

def second_smallest_item_better_way(l:list):
    l2 = sorted(l)
    return l2[1]


numbers_1= [2,4,5,8,1,9,5,6,7]
print(second_smallest_item_better_way(numbers_1))
print(numbers_1)
############ [:]
a = [1,2,3]
b = a
a[0] = 10
print(b) # [10, 2, 3]

c = [1,2,3]
d = c[:]
c[0] = 10
print(c) # [10, 2, 3]
print(d) # [1, 2, 3] if a changed d does not change 

############ 

