# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


import math

N = int(input('Введите число N: '))
def prime_factor(num):
    result_list = []
    i = 2
    while i <=math.ceil(num**2):
        if i%i == 0 and num%i == 0:
            result_list.append(i)
            num /= i
        else:
            i+=1
    return result_list

print(prime_factor(N))