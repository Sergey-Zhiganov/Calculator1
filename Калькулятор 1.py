import math
choose = 0
def two_numbers():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    return a, b
def one_number():
    a = float(input('Введите число: '))
    return a
def f_one(a, b):
    c = a+b
    return c
def f_two(a, b):
    c = a-b
    return c
def f_three(a, b):
    c = a*b
    return c
def f_four(a, b):
    if b != 0:
        c = a/b
    else:
        c = 'На ноль делить нельзя'
    return c
def f_five(a):
    b = float(input('Введите степень: '))
    c = a**b
    return c
def f_six(a):
    if a >= 0:
        c = math.sqrt(a)
    else:
        c = 'Нужно ввести число не меньше 0'
    return c
def f_seven(a):
    if a >= 0:
        c = math.factorial(int(a))
    else:
        c = 'Нужно ввести число не меньше 0'
    return c
def f_eight(a):
    c = math.sin(a)
    return c
def f_nine(a):
    c = math.cos(a)
    return c
def f_ten(a):
    c = math.tan(a)
    return c
while True:
    print('1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Возведение в степень\n6 - Квадратный корень\n7 - Факториал\n8 - Синус\n9 - Косинус\n10 - Тангенс\n11 - Выйти')
    choose = int(input('Операция: '))
    match choose:
        case 1:
            a, b = two_numbers()
            c = f_one(a, b)
        case 2:
            a, b = two_numbers()
            c = f_two(a, b)
        case 3:
            a, b = two_numbers()
            c = f_three(a, b)
        case 4:
            a, b = two_numbers()
            c = f_four(a, b)
        case 5:
            a = one_number()
            c = f_five(a)
        case 6:
            a = one_number()
            c = f_six(a)
        case 7:
            a = one_number()
            c = f_seven(a)
        case 8:
            a = one_number()
            c = f_eight(a)
        case 9:
            a = one_number()
            c = f_nine(a)
        case 10:
            a = one_number()
            c = f_ten(a)
        case _:
            break
    print('Ответ: ', c)