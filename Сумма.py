def sum_digits(number):
    sum = 0
    while number != 0:
        a = number % 10
        sum += a
        number = number // 10
    return sum
number = int(input("Введите положительное число: "))
if number >= 0:
    sum = sum_digits(number)
    print(sum)
else:
    print('Число меньше 0')