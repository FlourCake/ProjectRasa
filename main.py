import sqlite3
connect = sqlite3.connect('example.db')

def createTable():
    mycursor = connect.cursor()
    mycursor.execute("CREATE TABLE coba (nama text)")
    connect.commit()

def insertInto():
    mycursor = connect.cursor()
    mycursor.execute("INSERT INTO coba VALUES ('pro')")
    connect.commit()

def selectFrom():
    mycursor = connect.cursor()
    mycursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pengguna'")
    # mycursor.execute("SELECT * FROM coba")
    print(len(mycursor.fetchall()))

selectFrom()