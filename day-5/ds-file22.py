#creating a csv file from keyboard
import os,csv
with open('dscsv3','w',newline='') as fo:
    x=csv.writer(fo,quoting=csv.QUOTE_NONNUMERIC,delimiter='|')   #writer object
    headers=('EMPNO','EMPNAME','EMPCITY')
    x.writerow(headers)
    ans='y'
    while ans=='y':
        eno=int (input('enter enumber '))
        ename=input('enter ename ')
        ecity=input('enter ecity ')
        m=(eno,ename,ecity)
        x.writerow(m)
        ans=input('wish to continue ..')
        
