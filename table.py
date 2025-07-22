import sqlite3
conn=sqlite3.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    U_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS OrderTable (
    O_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    C_ID INTEGER,
    Amount REAL NOT NULL,
    Date TEXT NOT NULL,
    FOREIGN KEY (C_ID) REFERENCES Customer(U_ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    P_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Description TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Payment (
    P_ID INTEGER PRIMARY KEY,
    Type TEXT NOT NULL,
    Amount REAL NOT NULL,
    FOREIGN KEY (P_ID) REFERENCES OrderTable(O_ID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Category (
    C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Picture TEXT,
    Description TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cart (
    C_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    U_ID INTEGER,
    FOREIGN KEY (U_ID) REFERENCES Customer(U_ID)
);
""")

print("All tables created successfully.\n")
try:
    total = int(input("Enter the number of customers to insert: "))
    for i in range(total):
        print(f"\n--- Customer {i+1} ---")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        cursor.execute("INSERT INTO Customer (Name, Email, Password) VALUES (?, ?, ?)", (name, email, password))

    conn.commit()
    print(f"\n✅ Successfully inserted {total} customer(s).")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    conn.close()
