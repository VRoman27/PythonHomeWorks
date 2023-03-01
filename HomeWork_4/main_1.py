# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

size_1 = int(input("Введите размер массива 1: "))
numbers_1 = list()
print("Заполните массив 1: ")
for index in range(size_1):
    numbers_1.append(int(input())) 

size_2 = int(input("Введите размер массива 2: "))
numbers_2 = list()
print("Заполните массив 2: ")
for index in range(size_2):
    numbers_2.append(int(input())) 



numbers_3 = set(numbers_1).intersection(set(numbers_2))

print(numbers_1)
print(numbers_2)
print(numbers_3)