import sqlite3
# Создаем базу данных
CONN_DB = 'new_sql_table.db'
# Подключаем базу данных и выводим в терминал базу данных и версию.
with sqlite3.connect(CONN_DB) as sql_connect:
    print(sql_connect)
    print(sqlite3.version)
#Создаем таблицу в базе данных
with sqlite3.connect(CONN_DB) as sql_connect:
    sql_table = """CREATE TABLE IF NOT EXISTS curs_it(
                Name_Curs VARCHAR(255) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Email VARCHAR(255) NOT NULL,
                Number_Mobile CHAR(25));
                """
    sql_connect.execute(sql_table)
# Добавляем значения в столбцы таблицы в базе данных Вариант 1
# with sqlite3.connect(CONN_DB) as sql_connect:
#     sql_table = "INSERT INTO curs_it VALUES(?, ?, ?, ?, ?)"
#     sql_connect.execute(sql_table, ("Python", "Alexander", "Brovco", "alexdevelop1991@gmail.com", "079660660"))
#     sql_connect.execute(sql_table, ("Java", "Slava", "Ivanov", "slavva@gmail.com", "076436789"))
#     sql_connect.execute(sql_table, ("C++", "Nica", "Petrova", "nicaaa@gmail.com", "078452390"))
#     sql_connect.execute(sql_table, ("JavaScript", "Oleg", "Sidorov", "oleggg2000@gmail.com", "060671043"))
#     sql_connect.execute(sql_table, ("JavaScript", "Nicolai", "Popa", "kolea1983@gmail.com", "078651209"))
#     sql_connect.execute(sql_table, ("JavaScript", "Olea", "Smirnova", "oleasmirnova@mail.ru", "069128065"))
#     sql_connect.execute(sql_table, ("Python", "Dima", "Vieru", "vieru2000@gmail.com", "068340701"))
#     sql_connect.commit()
# Вариант 2
# curs_it = [
#     ("Python", "Alexander", "Brovco", "alexdevelop1991@gmail.com", "079660660"),
#     ("Java", "Slava", "Ivanov", "slavva@gmail.com", "076436789"),
#     ("C++", "Nica", "Petrova", "nicaaa@gmail.com", "078452390"),
#     ("JavaScript", "Oleg", "Sidorov", "oleggg2000@gmail.com", "060671043"),
#     ("JavaScript", "Nicolai", "Popa", "kolea1983@gmail.com", "078651209"),
#     ("JavaScript", "Olea", "Smirnova", "oleasmirnova@mail.ru", "069128065"),
#     ("Python", "Dima", "Vieru", "vieru2000@gmail.com", "068340701")
# ]
#
# with sqlite3.connect(CONN_DB) as sql_connect:
#     sql_table = "INSERT INTO curs_it VALUES(?, ?, ?, ?, ?)"
#     for i in curs_it:
#         sql_connect.execute(sql_table, i)
#     sql_connect.commit()
# Получение конкретную информацию из таблицы
with sqlite3.connect(CONN_DB) as sql_connect:
    select = "SELECT * FROM curs_it WHERE Name_Curs = 'JavaScript'"
    data = sql_connect.execute(select)
    sql_connect.commit()
    print('All information about JavaScript: ')
    for i in data:
        print(i)
# Обновляем данные в таблицы
with sqlite3.connect(CONN_DB) as sql_connect:
    update = "UPDATE curs_it SET Number_Mobile  = 079991299 WHERE First_Name = 'Dima'"
    update2 = sql_connect.execute(update)
    select = "SELECT * FROM curs_it"
    data = sql_connect.execute(select)
    sql_connect.commit()
    print('After update:')
    for i in data:
        print(i)

with sqlite3.connect(CONN_DB) as sql_connect:
    delete = " DELETE FROM curs_it WHERE First_Name =  'Alexander'"
    delete2 = sql_connect.execute(delete)
    select = "SELECT * FROM curs_it"
    data = sql_connect.execute(select)
    sql_connect.commit()
    print('After delete: ')
    for i in data:
        print(i)




