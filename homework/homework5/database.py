from statistics import mean
database = []
finish = {}

for j in range(1):

    s_name = input('Имя студента:')
    finish.update({'Имя студента:' :  s_name})

    for i in range(0, 4):
        dis_name = input('Дисциплина:')
        mark = int(input('Оценка:'))

    finish.update({dis_name : mark})

    database.append(finish.copy)

print(database)




