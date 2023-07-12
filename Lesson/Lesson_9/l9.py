import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))

x = datetime.datetime(2020, 5, 17)
print(x)

     # математические функции
x = min(5, 10, 25)
y = max((5, 10, 25))

print(x)
print(y)
# Функция  abs() возвращает абсолютное (положительное) значение указаного числа.
x = abs(-7.25)
# Функция pow(x, y) возвращает значение x в степени y
x = pow(4, 3)


# Модуль Math расширяет список магических функции
# Чтобы использовать его нужно импортировать
import math
# Напиример метод math.sqrt() возвращает квадратный корень числа
x = math.sqrt(64)
# Метод math.ceil() округляет число в большую сторону до ближайщего целого числа,
# Метод math.floor() округляет число в меньшую сторону  до ближайщего целого числа.
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
