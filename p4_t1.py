
from random import random
y = 10

def average(a):
    s = 0
    for i in range(y):
        s += a[i]
    return s/y

arr = [0] * y
for i in range(y):
    arr[i] = int(random() * 100)
b = average(arr)
print(arr)
print(b)