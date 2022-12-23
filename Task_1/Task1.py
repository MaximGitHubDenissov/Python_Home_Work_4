# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# 1-й вариант решения
import math
accuracy = input('Введите точность: ')
num = len(str(accuracy))-2
my_string = str(math.pi)
print(my_string[:my_string.find('.')+(num+1)])

# 2-й вариант решения
from decimal import*
accuracy = input('Введите точность: ')
num = Decimal(str(accuracy)).as_tuple().exponent*(-1)
print(num)
my_string = str(math.pi)
print(my_string[:my_string.find('.')+(num+1)])
