import sqlite3

try:
    # Поключения к базе данных
    CONN_DB = sqlite3.connect('sql_table.db')
    cursor = CONN_DB.cursor()
    # Создание таблицы
    cursor.execute('DROP TABLE IF EXISTS curs_it')
    # Параметры таблицы название столбцов
    table = """CREATE TABLE curs_it(
                Name_Curs VARCHAR(255) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Email VARCHAR(255));
                """
    cursor.execute(table)
    print('Table Сreate')

    # Добавляем значения в таблицу
    cursor.execute('''INSERT INTO curs_it VALUES ("Python", "Alexander", "Brovco", "alexdevelop1991@gmail.com");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("Java", "Slava", "Ivanov", "slavva@gmail.com");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("C++", "Nica", "Petrova", "nicaaa@gmail.com");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("JavaScript", "Oleg", "Sidorov", "oleggg2000@gmail.com");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("JavaScript", "Nicolai", "Popa", "kolea1983@gmail.com");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("JavaScript", "Olea", "Smirnova", "oleasmirnova@mail.ru");''')
    cursor.execute('''INSERT INTO curs_it VALUES ("Python", "Dima", "Vieru", "vieru2000@gmail.com");''')

    # Получаем данные из таблицы
    print('Data Insert in the table:')
    data = cursor.execute("""SELECT * FROM curs_it
                             WHERE Name_Curs = 'JavaScript'""")
    for row in data:
        print(row)

    # Обновляем данные в таблице
    update = cursor.execute("""UPDATE curs_it SET Email = 'koleaaaaa@gmail.com' WHERE First_Name = 'Nicolai'""")

    # #Получение всех данных с таблицы
    all_data = cursor.execute("""SELECT * FROM curs_it""")
    print("Table Curs It after Update:")
    for row in all_data:
        print(row)

    #Удаляем из таблице
    delete_data = cursor.execute("""DELETE FROM curs_it WHERE First_Name = 'Slava'""")

    all_data = cursor.execute("""SELECT * FROM curs_it""")
    print("Table Curs It after Delete:")
    for row in all_data:
        print(row)


    CONN_DB.commit()

    cursor.close()

except sqlite3.Error as Error:
        print('Error occured -', Error)
finally:
    if CONN_DB:
        CONN_DB.close()
        print('SQLite Connection closed')











