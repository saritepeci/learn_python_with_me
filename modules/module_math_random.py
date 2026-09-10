import math

print(math.sqrt(144))

# if you do not import directly:
print("Pi is before imported", math.pi )

#Now is imported pi:
from math import pi
print("Pi is", math.pi )


#you need to random.xxxx --->>> now samely r.xxxx  This is samely namespace
import random as r

print(r.randint(10,222)) 


#tabulate