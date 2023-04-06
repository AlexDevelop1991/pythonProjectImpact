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
               Last_Name CHAR(25));"""
    cursor.execute(table)
    print('Table is Ready')
    cursor.execute('''INSERT INTO Impact VALUES (stars91@gmail.com, Alexander, Brovco)''')
    cursor.execute('''INSERT INTO Impact VALUES (, Alexander, )''')
    cursor.execute('''INSERT INTO Impact VALUES (, Brovco)''')
    # Display data inserted
    print('Data Insert in the table:')
    data = cursor.execute('''SELECT * FROM Impact''')
    for row in data:
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
