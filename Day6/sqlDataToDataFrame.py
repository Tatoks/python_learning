import pandas as pd
import mysql.connector

# load data from mysql database

con = mysql.connector.connect(host="localhost", user='root', passwd='root', auth_plugin='mysql_native_password', database = 'univdb')
emp_data=pd.read_sql('select d.dept_id, d.dept_code from department d', con)
print(emp_data)
print(type(emp_data))
