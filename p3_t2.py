a=float(input("Введите a"))
b=float(input("Введите b"))
c=float(input("Введите c"))
if(a+b<c or c+a<b):
  print("Треугольника не существует")
elif(a==b and a==c):
  print("Равносторонний")
elif(a==b or a==c or b==c):
  print("Равнобедренный")
else:
  print("Разносторонний")
