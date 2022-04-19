#insert records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

s1='insert into mytable values (100,"computer")'
s2='insert into mytable values (101,"keyboard")'
s3='insert into mytable values (102,"monitor")'
y.execute(s1)
y.execute(s2)
y.execute(s3)

#for all dml operations (update, insert, delete) - we need to commit
x.commit()

y.close()
x.close()

