"""
    Name: db_library.py
    Author: Jessica Soler
    Date: 1/20/25
    Purpose: CRUD module for Jessica's Library Database
"""

# Import sqlite3 database library
import sqlite3
from tkinter import messagebox

DATABASE = 'library.db'

#---SQL STATEMENTS--------------------------------------------------------------SQL STATEMENTS----#
CREATE_AUTHOR_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_author (
        auth_id INTEGER PRIMARY KEY AUTOINCREMENT,
        auth_fname TEXT,
        auth_lname TEXT
    );
"""

CREATE_BOOK_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_book (
        bk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bk_title TEXT,
        bk_genre TEXT,
        bk_rating INTEGER,
        bk_pub_date TEXT,
        auth_id INTEGER,
        CONSTRAINT fk_author
            FOREIGN KEY (auth_id)
            REFERENCES tbl_author(auth_id)
            ON DELETE CASCADE
    );
"""

INSERT_AUTHOR = """
    INSERT INTO tbl_author (auth_fname, auth_lname) VALUES (?, ?);
"""

INSERT_BOOK = """
    INSERT INTO tbl_book (bk_title, bk_genre, bk_rating, bk_pub_date, auth_id) VALUES (?, ?, ?, ?, ?);
"""

FETCH_ALL_BOOKS = "SELECT * FROM tbl_book;"
FETCH_BOOK = "SELECT * FROM tbl_book WHERE bk_id = ?;"
DELETE_BOOK = "DELETE FROM tbl_book WHERE bk_id = ?;"
UPDATE_BOOK = "UPDATE tbl_book SET bk_title = ?, bk_genre = ?, bk_rating = ?, bk_pub_date = ?, auth_id = ? WHERE bk_id = ?;"
CLEAR_BOOKS = "DELETE FROM tbl_book;"

#---FUNCTIONS--------------------------------------------------------------------FUNCTIONS----#
def create_tables():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_AUTHOR_TABLE)
        cursor.execute(CREATE_BOOK_TABLE)

def add_author(auth_fname, auth_lname):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_AUTHOR, (auth_fname, auth_lname))
        messagebox.showinfo("Author Added", "Author has been added.")

def add_book(bk_title, bk_genre, bk_rating, bk_pub_date, auth_id):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_BOOK, (bk_title, bk_genre, bk_rating, bk_pub_date, auth_id))
        messagebox.showinfo("Book Added", "Book has been added.")

def fetch_books():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        records = cursor.execute(FETCH_ALL_BOOKS).fetchall()
        return records

def fetch_book(bk_id: int):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        book = cursor.execute(FETCH_BOOK, (bk_id,)).fetchone()
        return book

def delete_book(bk_id: int):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_BOOK, (bk_id,))
        messagebox.showinfo("Book Deleted", "Book has been deleted.")

def save_book(bk_id, bk_title, bk_genre, bk_rating, bk_pub_date, auth_id):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(UPDATE_BOOK, (bk_title, bk_genre, bk_rating, bk_pub_date, auth_id, bk_id))
        messagebox.showinfo("Book Updated", "Book has been updated.")

# def clear_books():
#     with sqlite3.connect(DATABASE) as connection:
#         cursor = connection.cursor()
#         cursor.execute(CLEAR_BOOKS)
#     messagebox.showinfo("Books Deleted", "All books have been deleted.")