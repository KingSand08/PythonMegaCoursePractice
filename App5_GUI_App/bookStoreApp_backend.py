import sqlite3
import sys, os

def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, relative_path))
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))
    return resolved_path
DB_PATH = resource_path("db/books.db")

def verifyPathIntegrity():
    global DB_PATH
    try:
        conn=sqlite3.connect(DB_PATH)
        conn.close()
    except sqlite3.OperationalError as e:
        DB_PATH = resource_path("App5_GUI_App/db/books.db")


def connect():
    verifyPathIntegrity()
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year text, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("INSERT INTO book values (NULL, ?, ?, ?, ?)", (title, author, year, isbn)) # NULL is id handled by its slef
    conn.commit()
    conn.close()
    
def delete(id):
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,)) 
    conn.commit()
    conn.close()
    
def update(id, title, author, year, isbn):
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id)) 
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()
# insert("The Sea", "John tablet", 1918, 913123132)
# insert("The Earth", "John Smith", 1918, 913123132)
# insert("The Sun", "John Smith", 1919, 913123133)
# delete("The Sea")
# print(search(isbn=913123132))
# update("The Moon", "John Smooth", 1917, 913123133, 3)
# print(view())
