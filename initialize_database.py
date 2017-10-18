import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE Stuff ('
               '    id INTEGER PRIMARY KEY,'
               '    v VARCHAR(120)'
               ')')
connection.commit()
cursor.close()

