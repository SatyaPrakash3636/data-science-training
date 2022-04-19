#bulk insertion of  records
import pymysql
x=pymysql.connect(host='localhost',user='root',password='welcome@123',database='accenture')
y=x.cursor()

#create a list of tuples - each tuple is one record
data=[]
k=1
while k<=3:
    eno=int(input('enter enumber '))
    ename=input('enter ename ')
    data.append((eno,ename))
    k+=1


#sql statement for bulk insertion
s="insert into mytable values (%s,%s)"

y.executemany(s,data)
x.commit()
y.close()
x.close()




