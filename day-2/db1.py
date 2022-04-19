#creating a table
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()
s='create table mytable (eno integer, ename character(10))'
y.execute(s)
y.close()
x.close()

