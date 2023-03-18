welcome = 'Привет добро пожаловать в игру  Угадай слово'
question = 'Вопрос:Как самый большой океан в мире?'
print(welcome)
print(question)

variant = (input('Ваш вариант:'))
answer = 'Тихий океан'

while variant != answer:
    if answer < variant:
        print('Не правильно попробуй ещё раз ')
    variant = input('Новый вариант:')

print('Поздравляю правильный ответ!')

















