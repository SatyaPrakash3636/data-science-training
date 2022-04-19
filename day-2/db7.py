#update  of  records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

s='update mytable set ename="AAA" where ename="aaa"'
y.execute(s)
x.commit()
y.close()
x.close()

