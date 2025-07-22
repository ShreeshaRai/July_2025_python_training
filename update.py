import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("UPDATE users SET name='DOG' WHERE id=1")
conn.commit()
conn.close()