# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

data = open('Task5_first_input.txt', 'w')
data.writelines('2x^2 + 3xy - 7')
data.close()

data2 = open('Task5_second_input.txt', 'w')
data2.writelines('3x4 - 5yz + 7x')
data2.close()

with open('Task5_first_input.txt', 'r') as file:
    my_str1 = file.readline()
print(my_str1)
with open ('Task5_second_input.txt', 'r') as file2:
    my_str2 = file2.readline()
print(my_str2)
with open('Task5_result.txt', 'w') as result:
    result.writelines(f'({my_str1}) + ({my_str2})')