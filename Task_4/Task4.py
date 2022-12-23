# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
coeff1 = str(random.randint(0,100))
coeff2 = str(random.randint(0,100))
coeff3 = str(random.randint(0,100))
degree = input('Введите степень многочлена: ')
print(f'{coeff1}*x^{degree} + {coeff2}*x + {coeff3} = 0' )

data = open('Task4_result.txt', 'w')
data.writelines(f'{coeff1}*x^{degree} + {coeff2}*x + {coeff3} = 0')
data.close()
