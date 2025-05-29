from database.connection import connect_to_db
from datetime import datetime

def insert():
    con = connect_to_db()
    cursor = con.cursor()
    issuer = input("Enter Issuer Name: ")
    book = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    doi = input("Enter Date of Issue (YYYY-MM-DD): ")
    dor = input("Enter Date of Return (YYYY-MM-DD): ")
    fine = int(input("Enter Fine (if any): "))

    query = "INSERT INTO data (Issuer_name, Book_name, Author_name, Date_of_issue, Date_of_return, Fine) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (issuer, book, author, doi, dor, fine))
    con.commit()
    con.close()
    print("Record Inserted.")

def display():
    con = connect_to_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM data")
    for row in cursor.fetchall():
        print(row)
    con.close()

def search():
    con = connect_to_db()
    cursor = con.cursor()
    book = input("Enter Book Name to search: ")
    query = "SELECT * FROM data WHERE Book_name = %s"
    cursor.execute(query, (book,))
    for row in cursor.fetchall():
        print(row)
    con.close()

def modify():
    con = connect_to_db()
    cursor = con.cursor()
    date = input("Enter date of issue (YYYY-MM-DD) for which to modify fine: ")
    new_fine = int(input("Enter new fine amount: "))
    query = "UPDATE data SET Fine = %s WHERE Date_of_issue = %s"
    cursor.execute(query, (new_fine, date))
    con.commit()
    con.close()
    print("Fine updated.")

def delete():
    con = connect_to_db()
    cursor = con.cursor()
    sno = input("Enter Serial Number to delete: ")
    query = "DELETE FROM data WHERE SNO = %s"
    cursor.execute(query, (sno,))
    con.commit()
    con.close()
    print("Record deleted.")