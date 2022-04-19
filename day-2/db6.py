#deletion  of  records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

s='delete from mytable where eno>700'
y.execute(s)
x.commit()
y.close()
x.close()

