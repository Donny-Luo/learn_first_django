# Install Mysql on your computer
# pip install mysql
# pip install my-connector
# pip install mysql-connctor-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'johnkaylou'

)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')