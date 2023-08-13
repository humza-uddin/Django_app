#install mysql
#pip install mysql
#pip install mysql-connector
#---Pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Powerful@123',
)   

#prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE VisumAcura")

print("Database has been Created!")