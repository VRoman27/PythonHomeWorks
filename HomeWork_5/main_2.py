# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    a += 1
    return sum(a, b-1) 

number_1 = int(input("Первое число: "))
number_2 = int(input("Второе число: "))

result = sum(number_1, number_2)
print(f"{number_1} + {number_2} = {result}")