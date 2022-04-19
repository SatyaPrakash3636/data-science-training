#displaying  of  records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

s='select * from mytable'
y.execute(s)
p=y.fetchall()
print ('%-10s%-10s' % ('ENUMBER','ENAME'))
for m in p:
    print ('%-10s%-10s' % (m[0],m[1]))
y.close()
x.close()

