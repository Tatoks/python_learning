import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("data.xls")
sheet = book.sheet_by_name("source")

# Establish a MySQL connection
connection = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysqlPython")

# Get the cursor, which is used to traverse the database, line by line
cursor = connection.cursor()

# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS orders")

# Create Table orders
cursor.execute("""CREATE TABLE orders(  
   cus_id INT NOT NULL AUTO_INCREMENT,  
   cus_firstname VARCHAR(100) NOT NULL,
   cus_product VARCHAR(100) NOT NULL,  
   cus_quantity VARCHAR(100) NOT NULL,  
   PRIMARY KEY ( cus_id )  
);  
""")

# Create the INSERT INTO sql query
query = """INSERT INTO orders (cus_firstname, cus_product, cus_quantity) VALUES (%s, %s, %s) """

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    name = sheet.cell(r, 0).value
    product = sheet.cell(r, 1).value
    quantity = sheet.cell(r, 2).value

    # Assign values from each row
    values = (name, product, quantity)

    # Execute sql Query
    cursor.execute(query, values)

    # Commit the transaction
    connection.commit()


# Close the cursor
cursor.close()



# Close the database connection
connection.close()

# Print results
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows - 1)
print("Imported", columns, "columns and", rows, "rows to MySQL!")
print("Executed Completed!!")
