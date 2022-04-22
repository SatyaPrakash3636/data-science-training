#joining the columns
import pandas as pd
#first data frame
data1=[('AAA',111),('BBB',222),('CCC',333)]
df1=pd.DataFrame(data1,columns=['NAME','AGE'])
print (df1)
print ()
#second data frame
data2=[('PPP',777),('QQQ',888),('RRR',999)]
df2=pd.DataFrame(data2,columns=['CITY','PIN'])
print (df2)

#concatenating data frames
df3=pd.concat([df1,df2],axis=1)
print (df3)



