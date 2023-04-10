import sqlite3

try:
    # Connect To DB and create a cursor
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('Db Init')
    # Write a query and execute it with cursor
    query = 'select sqlite_version();'
    cursor.execute(query)
    # Fetch and output result
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    cursor.execute('DROP TABLE IF EXISTS Impact')
    # Creat table
    table = """CREATE TABLE Impact(
               Email VARCHAR(255) NOT NULL,
               First_Name CHAR(25) NOT NULL,
               Last_Name CHAR(25));
               """
    cursor.execute(table)
    print('Table is Ready')
    cursor.execute('''INSERT INTO Impact VALUES ("stars91@gmail.com", "Alexander", "Brovco");''')
    cursor.execute('''INSERT INTO Impact VALUES ("blabla@gmail.com", "Alexander", "A");''')
    cursor.execute('''INSERT INTO Impact VALUES ("last@gmail.com", "Brovco", "B");''')
    # Display data inserted
    print('Data Insert in the table:')
    data = cursor.execute("""SELECT * FROM Impact
                          WHERE First_Name = 'Alexander'""")
    for row in data:
        print(row)

    update = cursor.execute("""UPDATE Impact SET Email = 'shadowstars@gmail.com' WHERE First_Name = 'Alexander'""")

    all_data = cursor.execute("""SELECT * FROM Impact""")
    print("Table Impact after Update:")
    for row in all_data:
        print(row)

    delete = cursor.execute("""DELETE FROM Impact WHERE First_Name = 'Alexander'""")

    delete_data = cursor.execute("""SELECT * FROM Impact""")
    print("Table Impact after Delete:")
    for row in delete_data:
        print(row)





# Commit your changes in the database
    sqliteConnection.commit()
    # Close the cursor
    cursor.close()
# Handle errors
except sqlite3.Error as error:
    print('Error occured -', error)
# Close DB Connection irrespective of success
# or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
