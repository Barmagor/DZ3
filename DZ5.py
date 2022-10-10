# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

n = int(input('Введите длину ряда: '))
i = 0
a=[]
for i in range (n):
    if i > 0:
        f1, f2 = f2, f1 + f2 
    if i == 0:
        f1 = f2 = 0
    if i == 1:
        f2 = 1
    a.append(f2)
print(a)
a.reverse()
print(a)
b=[]
for i in range (n):
    if i > 0:
        f1, f2 = f2, f1 + f2 
    if i == 0:
        f1 = f2 = 0
    if i == 1:
        f2 = 1
    b.append(f2)
print(b)
b.pop(0)
c=a+b
print(c)
for j in range (8):
    if j%2 != 0:
        c[j]=c[j]*(-1) 
print(c)

