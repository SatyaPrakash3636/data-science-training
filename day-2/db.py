import pymysql

conn = pymysql.connect(
    host="192.168.225.201", user="satya", password="satya", database="python"
)

cursor = conn.cursor()

stmt1 = "show tables"
stmt2 = "select * from scripts"

cursor.execute(stmt2)

data1 = cursor.fetchall()

print(data1)
