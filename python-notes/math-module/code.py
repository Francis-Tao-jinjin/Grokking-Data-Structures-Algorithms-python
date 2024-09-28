import random
import math

def f1():
    print('abs(-45):', abs(-45))
    li = [random.randint(0, 20) for i in range(10)]
    print('li:', li)
    print([(math.ceil(i / 3), i, math.floor(i/3)) for i in li])

f1()
