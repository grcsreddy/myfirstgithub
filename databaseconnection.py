import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "chandra",
    passwd="1234",
    database='sakila')

mycursor = mydb.cursor()
mycursor.execute("select * from actor ")
result =mycursor.fetchone()
for i in result:
    print(i)
