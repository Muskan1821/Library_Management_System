import mysql.connector as mc

def connect_to_db():
    try:
        con = mc.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="book_data"
        )
        return con
    except mc.Error as e:
        print("Connection Error:", e)
        return None

def create_db():
    con = mc.connect(
        host="localhost",
        user="root",
        password="your_password"
    )
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS book_data")
    con.close()

def create_table():
    con = connect_to_db()
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            SNO INT AUTO_INCREMENT PRIMARY KEY,
            Issuer_name VARCHAR(200) NOT NULL,
            Book_name VARCHAR(200) NOT NULL,
            Author_name VARCHAR(200) NOT NULL,
            Date_of_issue DATE NOT NULL,
            Date_of_return DATE NOT NULL,
            Fine INT
        )
    """)
    con.commit()
    con.close()