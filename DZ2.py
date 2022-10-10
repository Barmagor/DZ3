#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = []
for i in range (0, 11):
    list.append(i)
print(list)
l=int(len(list)/2)
count=0
for j in list:
    x=(list[0+j] * list[-1-j])
    count +=1
    if count > l:
        break
    else: 
        print(x, end=" ")

