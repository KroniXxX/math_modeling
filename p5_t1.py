import math 
a=float(input("Число: "))
n=int(input("Степень: "))
print(math.pow(a,n))









def fibonacci(n):
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(10))