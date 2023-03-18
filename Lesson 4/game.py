a = int(input('Введи цифру:'))
b = 20
while a != b:
    if b > a:
        print('Не правильно слишком маленькое')
    else:
        print('Не правильно слишком большое')
    a = int(input('Введи цифру:'))
print('You win')



