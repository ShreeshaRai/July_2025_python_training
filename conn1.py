import mysql.connector
def insert_data(id,name,password,email):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="shreesha_cse"
    )
    print(mydb)
    mycursor=mydb.cursor()
    sql="INSERT INTO user(id,name,password,email) VALUES(%s,%s,%s,%s)"
    
    val=(id,name,password,email)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")
id=input("enter the id")
name=input("enter the name")
password=input("enter the password")
email=input("enter the email")
insert_data(id,name,password,email)

