# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def powNum(num, deg):
    if deg == 0:
        return 1
    return powNum(num, deg-1) * num

number = int(input("Введите число: "))
degree = int(input("Введите степень: "))

result = powNum(number, degree)
print(result)