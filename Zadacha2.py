# Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N.
# 
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

