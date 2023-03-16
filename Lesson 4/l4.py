
                     #While цикл
a = 1

while a < 18:

    print('вам исполнилось' + str (a) + 'годы')

    a += 1

print('Поздравляем с совершенолетием')

                       #For цикл
for c in range (1, 18):

    print( 'Вы ещё не достигли совершенолетия')

    print('Вам недавно исполнилось ', c)

    print('Осталось', 18 - c, 'лет')

print('Поздравляю с совершенолетием')

                          #Проверить на четные и нечетные
par = []
impar = []
for i in range(20):
    if i % 2 == 0:
        par.append(1)
    else:
        impar.append(1)


txt = "cool boys"

print('cool' in txt)

txt = 'Лучшие вещи  в жизни бесплатны!'
if 'бесплатный' in txt:
    print('Да бесплатный присутсвует')
                          #Изменение строк
a = 'Hello World!'
print(a.upper())
print(a.lower())
print(a.strip()) # пробелы удаляет в конце и начале
print(a.replace('H', 'F'))

a = 'Hello'
b = 'World'
c = a + b
print(c)

a = 'Hello '
b = 'World'
c = a + b
print(c)

age = 36
txt = f'My name jonh, and I {age}'
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = 'Я хочу {0} единиц товара {1} за {2} долларов'
print(myorder.format(quantity, itemno, price))