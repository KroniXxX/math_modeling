from random import random
import numpy as np

y = 10

def average(a):
  s = 1
  for i in range(y):
    s *= a[i]
  return s

def np_mpl(a):
  return np.prod(a)

arr = [0] * y
for i in range(y):
    arr[i] = int(random() * 100)

b = average(arr)
c = np_mpl(arr)

print(arr)
print(b, c)