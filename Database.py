import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='xavis')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection succesfully created!")