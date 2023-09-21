def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        print('Введите числа больше 0')
    else:
        print('Площадь прямоугольника: ', width*height)

width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
rectangle_area(width, height)