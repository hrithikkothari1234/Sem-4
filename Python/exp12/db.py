import MySQLdb 
  
try: 
    db_connection = MySQLdb.connect("localhost","root","password","dbname") 
except: 
    print("Can't connect to db") 

print("Connected db") 

cursor = db_connection.cursor() 

sql = "CREATE TABLE IF NOT EXISTS STUDENT (roll_no INT, name VARCHAR(20), attendance INT, marks INT )"
cursor.execute(sql)

cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s)",(8677, 'Hritik', 50, 70))

cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s)",(8678, 'abc', 60, 30))

cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s)",(8679, 'def', 70, 50))

cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s)",(8670, 'ghi', 80, 90))

cursor.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s)",(8671, 'jkl', 90, 60))

cursor.execute("SELECT * FROM STUDENT")
print("After Inserting \n",cursor.fetchall())

cursor.execute("UPDATE STUDENT SET marks = %s WHERE roll_no = %s",(100, 8677))

cursor.execute("SELECT * FROM STUDENT")
print("After updating \n",cursor.fetchall())

cursor.execute("DELETE FROM STUDENT WHERE roll_no = 8671")

cursor.execute("SELECT * FROM STUDENT")
print("After Deleting \n",cursor.fetchall())

db_connection.close() 