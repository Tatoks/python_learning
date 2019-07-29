############################################################
# SQLITE3 DATABASE CONNECTION AND EXCEPTION HANDLING

import sqlite3 as lite
import sys

# create sqlite connection and retrieve the sqlite version
con = None

try:
    con = lite.connect('common.db')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSIO()')
    data = cur.fetchone()
    print ("SQLite version: %s" % data)
except lite.Error as e:
    print("Exception : lite.Error")
    print ("Error %s:" % e.args[0])
except Exception as e:
    print("Exception")
    print(e)
    sys.exit(1)
finally:
    if con:
        con.close()

############################################################
# MYSQL DATABASE CONNECTION AND EXCEPTION HANDLING

import mysql.connector

con = None
try:
    # create MYSQL connection & create commondb by default
    con = mysql.connector.connect(host='localhost', user='root', passwd='hello123', auth_plugin='mysql_native_password',
                                  database='commondb')
    cur = con.cursor()

    # fetch MYSQL version
    print("-----------------------------------------")
    cur.execute('SELECT VERSION()')
    data = cur.fetchone()
    print ("MYSQL version: %s" % data)
except mysql.connector.Error as err:
    print("mysql exception: {}".format(err))
except Exception as e:
    print ("Error %s:" % e.args[0])
    sys.exit(1)
finally:
    if con:
        con.close()
########################################################### 