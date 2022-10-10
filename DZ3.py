#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = []
for i in range (12, 123, 20):
    list.append(i/9)
print(list)
len1=int(len(list))
j=0
max=0
min=123
while j < len1:
    a=int(list[j]*10)%10
    if a > max:
        max = a
    if a < min:
        min = a    
    j+=1
print(max-min)
