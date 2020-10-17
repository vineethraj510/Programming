import mysql.connector

con_obj = mysql.connector.connect(host = 'hostname',user = 'username', password = 'password')   # create a connection object

cur_obj = con_obj.cursor()  # create a cursor object

cur_obj.execute("CRUD operations") # execute query operations
result = cur_obj.fetchall()

# for showing databases we write "show databases"
