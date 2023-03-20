
print('Привет, добро пожаловать в игру "Угадай слово"')
print('Вопрос: Какой самый большой океан в мире?')

variant = input('Ваш вариант:').lower()

answer = 'тихий'

while variant != answer:
    if answer < variant:
        print('Не правильно попробуй ещё раз ')
    variant = input('Новый вариант:').lower()

print('Поздравляю правильный ответ!')

















