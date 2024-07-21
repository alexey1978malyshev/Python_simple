# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8
# (*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print
# Примеры/Тесты:
# 10     -> 1,2,4,8,
# 10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,
import math

n = int(input("Введите N: "))
count = 0
exponent = 0
out_srt = ''
while exponent < n:
    exponent = 2 ** count
    count += 1
    if exponent < n:
        # print(exponent)
        out_srt += str(exponent) + ','
print(out_srt)
#
#
# Пример идеального решения
#
# Задача 10
#
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)
#
# Задача 12
#
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
#
# Задача 14
#
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

