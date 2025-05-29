from database.connection import create_db, create_table
from operations.book_operations import insert, display, search, modify, delete

def menu():
    create_db()
    create_table()
    while True:
        print("\n--- Library Management System ---")
        print("1. Insert Record")
        print("2. Display Records")
        print("3. Search Book")
        print("4. Modify Fine")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert()
        elif choice == '2':
            display()
        elif choice == '3':
            search()
        elif choice == '4':
            modify()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")