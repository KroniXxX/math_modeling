from math import sqrt
a=float(input("Введите a"))
b=float(input("Введите b"))
c=float(input("Введите c"))
d=b**2-4*a*c
if(d<0):
  print("нет корней")
elif(d==0):
  x=-b/2*a
  print (x)
elif(d>0):
  x1=(-b+sqrt(d))/2*a
  x2=(-b-sqrt(d))/2*a
  print(x1,x2)

