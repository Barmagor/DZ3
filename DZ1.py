# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list = []
for i in range (0, 11):
    list.append(i)
print(list)
sum = 0
for i in list:
    if i%2 !=0:
        sum=i+sum
    i+=1
print(sum)
