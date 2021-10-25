a = int(input("Введите целое число: "))
b = 0
 
while a > 0:
  d = a % 10
  
  a = a // 10
  b = b * 10
  b = b + d  
 
print('"Обратное" ему число:', b)