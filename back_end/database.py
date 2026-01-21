import sqlite3

def get_connection():
    connect=sqlite3.connect('task.db')
    cursor=connect.cursor()
    return cursor,connect

def disconnect(connect):
    connect.close()
    return True

cursor,connect=get_connection()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks(
               ID INTEGER,
               Title TEXT,
               Descripcion Text,
               State INTEGER,
               Created TEXT,
               Last_Update TEXT
               )
'''
)

disconnect(connect)