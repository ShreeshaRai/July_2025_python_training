import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age integer
)
''')
conn.commit()
conn.close()
