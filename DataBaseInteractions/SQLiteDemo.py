import sqlite3 as lite
import sys

# We are suing SQLite package to connect to DB and run commands
# Data files are created under folder: ..\Day5\DataBaseInteractions
# Demo code for connect to db and do CURD operations
# Install SQL community edition to view files created - commondb, database.db
con = None
try:
    # create sqlite connection and create commonDB by default
    con = lite.connect('commondb') # Any db name you wanna use
    cur = con.cursor() # Cursor objects helps establishing connection

    # fetch sqlite version
    print("--------------------------------------")
    cur.execute('SELECT SQLITE_Version()')  # get SQLite version installed
    data = cur.fetchone()
    print("SQLite version: %s " % data)
except Exception as e:
    print("Error:", e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()


# CURD Operations demo

con = lite.connect('commondb')
with con:
    cur = con.cursor()
    cur.execute('DROP table IF Exists employee') # Delete table if exists
    print("=------------------------------=")
    print("CREATE TABLE employee(Id INT, Name TEXT)")
    cur.execute("CREATE TABLE employee(Id INT, Name TEXT)") # Create table with schema

    cur.execute("INSERT INTO employee VALUES(1, 'Suni')") # Insert into table
    cur.execute("INSERT INTO employee VALUES(2, 'Saini')")
    cur.execute("INSERT INTO employee VALUES(3, 'Geloth')")
    cur.execute("INSERT INTO employee VALUES(4, 'Abhi')")

    cur.execute("SELECT * FROM employee") # Fetch data from table
    row = cur.fetchall()
    for r, n in row:
        print(str(r), " : ", str(n))

    # delete data from employee where id = 3
with con:
    cur.execute('Delete FROM employee where id=3')
    #fetch data from employee
    cur.execute('Select * from employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)

# update data for employee where emp_id=4

with con:
    cur.execute("update employee set name='Robert' where id=4")
    # fetch data from employee
    cur.execute('Select * from employee')
    rows = cur.fetchall()
    for row in rows:
        print(row)