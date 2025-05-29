# 📚 Library Management System

A Python-based **Library Management System** that connects to a MySQL database to manage book records, issue/return dates, and fines. Built with clean modular code, it's designed for students, librarians, and anyone learning Python with databases.

---

## ✨ Features

- 📘 Add new books with issue and return dates
- 🔍 Search for books by name
- 🛠️ Modify fines based on issue date
- 📋 View all book records in a structured format
- 🗑️ Delete specific entries
- 🎛️ Menu-driven CLI interface

---

## 🧱 Project Structure

```
LibraryManagementSystem/
├── database/
│   └── connection.py          # MySQL connection and DB/table setup
├── operations/
│   ├── book_operations.py     # CRUD operations for book data
│   └── utils.py               # Date validation helper
├── main/
│   └── menu.py                # Command-line menu interface
```

---

## ⚙️ How to Run

### 1. Install Requirements

Make sure you have Python and MySQL installed.

Then install the Python package:
```bash
pip install mysql-connector-python
```

### 2. Set Up MySQL

Create the database manually, or let the program create it for you (it runs `CREATE DATABASE` and `CREATE TABLE`).

Update your MySQL password in `database/connection.py`:
```python
password="your_mysql_password"
```

### 3. Run the Program

```bash
python main/menu.py
```

---

## 💡 Future Improvements

- Add a graphical user interface (GUI) using Tkinter or PyQt
- Add user authentication for librarians vs students
- Export data to CSV or PDF reports
- Host online using Flask or Django

---

## 👩‍💻 Developed By

**Muskan Agarwal**  


---

## 📜 License

This project is for educational purposes and learning use only.
