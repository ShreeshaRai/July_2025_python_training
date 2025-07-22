import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
n=int(input("enter the total number of users to insert"))
for i in range(n):
    print(f"enter details for user{i+1}")
    name=input("enter the name:")
    age=int(input("enter age:"))
    cursor.execute("INSERT INTO users(name,age) VALUES(?,?)",(name,age))
conn.commit()
conn.close()
