# STEPS OF CONNECTING AND USING A SQL DB
#   1. Connect to the DB
#   2. Create a cursor object (like pointer to access rows from a DB)
#   3. Submit an SQL query
#   4. Commit changes to the DB
#   5. Close the connection

import psycopg2

PROJDIR = "./App_Project_Practice/interacting_with_databases/"
PROJDIR_DB = PROJDIR + "/db/"

def createTable():
    # Connect to the DB
    conn=sqlite3.connect(PROJDIR_DB + "lite.db")

    # Create cursor object to DB
    cur=conn.cursor()

    # Subit an SQL query
    # TYPES :: -> TEXT = String, INTEGER = int, REAL = float
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes to the DB
    conn.commit()

    # Close the connection
    conn.close()
    
def insertToTable(db_path, item, quantity, price):
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    # By putting the ?,?,? we are helping prevent SQL Injections utilizing the string strategy
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price)) 
    conn.commit()
    conn.close()

def deleteFromTable(db_path, item):
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,)) 
    conn.commit()
    conn.close()
    
def update(db_path, item, quantity, price):
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item)) 
    conn.commit()
    conn.close()
    
def viewDB(db_path):
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


db_path = PROJDIR_DB + "lite.db"
# insertToTable(db_path, 'Wine Glass', 8, 10.5)
# deleteFromTable(db_path, 'Wine Glass')
update(db_path, 'Wine Glass', 5, 15.5)
print(viewDB(db_path))
