#creating a csv file from keyboard
import os,csv
with open('dscsv','w',newline='') as fo:
    x=csv.writer(fo)   #writer object
    headers=('EMPNO','EMPNAME','EMPCITY')
    x.writerow(headers)
    s1=(111,"AAA","hyd")
    s2=(222,"BBB","delhi")
    s3=(333,"CCC","pune")
    x.writerow(s1)
    x.writerow(s2)
    x.writerow(s3)
    
    
