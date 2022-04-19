import pymysql

conn = pymysql.connect(
    host="192.168.225.201", user="satya", password="satya", database="world"
)

cursor = conn.cursor()

stmt1 = "show tables"
stmt2 = "select * from city"

cursor.execute(stmt2)

data1 = cursor.fetchall()

for data in data1:
    print(data)
