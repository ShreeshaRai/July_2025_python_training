import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="shreesha_cse"
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("INSERT INTO user(id,name,password,email)values(6,'mulumul','mukul','hggj@gmail.com')")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
