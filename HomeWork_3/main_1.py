# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

size = int(input("Введите длину массива: "))
array = []
for i in range(size):
    array.append(int(input(f"Введите элемент №{i}: ")))
print(array)

number = int(input("Введите число: "))
count = 0
for i in range(len(array)):
    if array[i] == number:
        count += 1
print(f"Число {number}  встречается {count} раз")