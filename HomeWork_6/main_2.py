# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

def indexInRange(array, min, max):
    result = []
    for index in range(len(array)):
        if min <= array[index] <= max:
            result.append(index)
    return result

size = 10
array = [randint(0, 20) for i in range(size)]
print(array)
minNum = int(input("Введите минимум: "))
maxNum = int(input("Введите максисум: "))
indexes = indexInRange(array, minNum, maxNum)
print(indexes)