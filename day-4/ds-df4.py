#create a data frame from a list thru input

#importing the libraries
import pandas as pd

#creating a list of ename and city tuples from keyboard
data=[]
ans='y'
while ans=='y':
    ename=input('enter ename ')
    ecity=input('enter ecity ')
    m=(ename,ecity)
    data.append(m)
    ans=input('repeat (y/n) ')

#store this data in a data frame
df=pd.DataFrame(data,columns=['ENAME','ECITY'])
print (df.to_string(index=False))

    
