# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progression(firsElement, delta, count):
    result = []
    for index in range(1, count):
        result.append(firsElement + (index - 1) * delta)
    return result

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность элементов: "))
N = int(input("Введите количество элементов: "))
array = progression(a1, d, N)
print(array)