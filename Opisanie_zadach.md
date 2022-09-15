* Задача 1

    Вычислить число c заданной точностью d

    Пример:

при $d = 0.001, π = 3.141.$

* Решение
import math
ppi = math.pi
n = float(input('Введите заданную точность '))
if n ==0.1:
    print(round(ppi,1))
elif n ==0.01:
    print(round(ppi,2))
elif n ==0.001:
    print(round(ppi,3))
elif n ==0.0001:
    print(round(ppi,4))
elif n ==0.00001:
    print(round(ppi,5))
elif n ==0.000001:
    print(round(ppi,6))
elif n ==0.000001:
    print(round(ppi,7))
elif n ==0.0000001:
    print(round(ppi,8))
elif n ==0.00000001:
    print(round(ppi,9))
elif n ==0.000000001:
    print(round(ppi,10))
elif n ==0.0000000001:
    print(round(ppi,11))
elif n ==0.00000000001:
    print(round(ppi,12))
elif n ==0.000000000001:
    print(round(ppi,13))
elif n ==0.0000000000001:
    print(round(ppi,14))
elif n ==0.00000000000001:
    print(round(ppi,15))
else:
    print(ppi)


* Задача №2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
* Решение
x = int(input("Введите натуральное число N: "))
i=2
list=[]
old = x
while i<=x:
    if x % i==0:
        list.append(i)
        x//=i
        i=2
    else:
        i+=1
print(list)


* Задача 3
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов
исходной последовательности.
* Решение:
list=[1,2,3,4,5,5,6,7,8,8]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)


















