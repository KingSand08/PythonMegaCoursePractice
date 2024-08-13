import sqlite3
import sys, os

def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, relative_path))
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))
    return resolved_path

class Database:
    def __init__(self):
        try:
            self.conn=sqlite3.connect(resource_path("db/books.db"))
        except sqlite3.OperationalError as e:
            self.conn=sqlite3.connect(resource_path("App5_GUI_App/db/books.db"))
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year text, isbn integer)")
        self.conn.commit()            

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book values (NULL, ?, ?, ?, ?)", (title, author, year, isbn)) # NULL is id handled by its slef
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,)) 
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id)) 
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows
    
    def __del__(self):
        self.conn.close()