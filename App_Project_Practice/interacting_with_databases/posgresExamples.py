# STEPS OF CONNECTING AND USING A SQL DB
#   1. Connect to the DB
#   2. Create a cursor object (like pointer to access rows from a DB)
#   3. Submit an SQL query
#   4. Commit changes to the DB
#   5. Close the connection

import psycopg2

def createDatabase(db_name):
    try:
        # Connect to the default database (e.g., postgres)
        conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'")
        conn.autocommit = True  # Required to execute CREATE DATABASE command
        cur = conn.cursor()

        # Check if the database already exists (the SELECT 1 is posing a true/false chack, if yes 1, is no
        #   None). pg_database is a system catalog table in PostgreSQL that contains information about all
        #   the databases on the server. It includes columns such as datname (the name of the database) and 
        #   others.
        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", [db_name]) # Grabs status 
        
        # Fetches the first row from the result of the query. If the database exists, this will return a row  
        #   with the value 1. If it does not exist, fetchone() will return None.
        exsists = cur.fetchone() 
        
        if not exsists:
            # Create the database if it doesn't exist
            cur.execute(f"CREATE DATABASE {db_name}")

        # Close the connection to the default database
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")
    
def deleteDatabase(db_name):
    # Connect to the PostgreSQL server (not to any specific database)
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='postgres123' host='localhost' port='5432'")
    conn.autocommit = True  # Required for DROP DATABASE command

    # Create cursor object
    cur = conn.cursor()

    try:
        # Drop the database
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    except psycopg2.Error as e:
        print(f"Error dropping database: {e}")
    
    # Close the cursor and connection
    cur.close()
    conn.close()

def createTable(db_name):
    createDatabase(db_name)
    # Connect to the DB
    conn = psycopg2.connect(f"dbname='{db_name}' user='postgres' password='postgres123' host='localhost' port='5432'")

    # Create cursor object to DB
    cur=conn.cursor()

    # Submit an SQL query
    # TYPES :: -> TEXT = String, INTEGER = int, REAL = float
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes to the DB
    conn.commit()

    # Close the connection
    conn.close()
    
def insertToTable(db_name, item, quantity, price):
    conn=psycopg2.connect(f"dbname='{db_name}' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    # By putting the ?,?,? we are helping prevent SQL Injections utilizing the string strategy
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price)) 
    conn.commit()
    conn.close()

def deleteFromTable(db_name, item):
    conn=psycopg2.connect(f"dbname='{db_name}' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) 
    conn.commit()
    conn.close()
    
def update(db_name, item, quantity, price):
    conn=psycopg2.connect(f"dbname='{db_name}' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item)) 
    conn.commit()
    conn.close()
    
def viewDB(db_name):
    conn=psycopg2.connect(f"dbname='{db_name}' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

# deleteDatabase('database1')
# createDatabase('database1')
# createTable('database1')
# deleteFromTable('database1', 'Wine')
# insertToTable('database1', 'Wine', 10, 100.50)
# update('database1', 'Wine', 5, 150.50)
# print(viewDB('database1'))