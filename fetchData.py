import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost',user="root",passwd="123456" , database= "telusko")
mycursor = connection.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
    print(i)
#show all database -----------
# for i in mycursor:
#     print(i)