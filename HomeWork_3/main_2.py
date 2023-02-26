# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

size = int(input("Введите длину массива: "))
array = []
for i in range(size):
    array.append(int(input(f"Введите элемент №{i}: ")))
print(array)

number = int(input("Введите число: "))
closeNumber = 1000000
index = None
for i in range(len(array)):
    if closeNumber >= abs(array[i]-number):
        closeNumber = abs(array[i]-number)
        index = i
print(f"Ближайшее к {number}: {array[index]}")