import mysql.connector
import mysql as mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)