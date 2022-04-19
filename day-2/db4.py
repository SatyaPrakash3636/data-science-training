#bulk insertion of  records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

with open('data.txt','r') as fo:
    mylist=[]
    for m in fo:
        m=m.strip()
        n=m.split('|')
        n=tuple(n)
        mylist.append(n)
    print (mylist)

s="insert into mytable values (%s,%s)"
y.executemany(s,mylist)
x.commit()
y.close()
x.close()
