# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N=int(input("Введи число:"))
print(N)
from random import randint
lst=[randint(1,N) for i in range(1,N)]
print(*lst)
x=int(input("Введи число x:"))
min=abs(int(x-lst[0]))
element=0
for i in range(len(lst)):
    number=abs(int(x-lst[i]))
    if number<min:
        min=number
        element=i
print(lst[element])


