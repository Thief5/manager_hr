import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'parolamysql'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dbproiect")

print("okkkkk")