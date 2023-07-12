a = input('Выберите язык/Choose language (ru/en): ')


while True:

    if a == 'ru':
        first_q = 'Как ты себя чувствуешь?'
        print(first_q)
        a1 = input()
        print('Отлично 😊')
        second_q = 'Что ты сегодня делал?'
        print(second_q)
        a2 = input()
        print('Очень хорошо что у вас был такой насыщенный день😎!!!')
        third_q = 'Какая твоя любимая музыка?'
        print(third_q)
        a3 = input()
        print('Мне тоже такая музыка нравиться🎵))')
        answer = input('Хотите ещё раз пообщаться?🙂 да или нет:')
        if answer == 'нет':
            break

    elif a == 'en':
        first_q = 'How do you feel?'
        print(first_q)
        a1 = input()
        print('Perfect 😊')
        second_q = 'What you were doing today?'
        print(second_q)
        a2 = input()
        print("That's great that you had such a wonderful day😎!!!")
        third_q = 'What is your favourite music ?'
        print(third_q)
        a3 = input()
        print('I like suck music too🎵')
        answer = input('Do you want to chat again?🙂 yes or no:')
        if answer == 'no':
            break










