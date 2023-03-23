from statistics import mean
database = []
finish = {}
mark_sum = 0
count = 0

for j in range(1):

    s_name = input('Имя студента:')
    finish.update({'Имя студента:' :  s_name})

    for i in range(0, 4):
        dis_name = input('Дисциплина:')
        mark = int(input('Оценка:'))
        finish.update({dis_name : mark})
        mark_sum += mark
        count += 1
x = str(mark_sum/count)
print(s_name + ' Средний бал:' + x)

database.append(finish.copy())

print(database)




