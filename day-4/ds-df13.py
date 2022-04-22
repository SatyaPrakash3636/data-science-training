#addition of  rows
import pandas as pd
#first data frame
data1=[('AAA',111),('BBB',222),('CCC',333)]
df1=pd.DataFrame(data1,columns=['NAME','AGE'])

print (df1)
print ()
#second data frame
data2=[('PPP',777),('QQQ',888),('RRR',999)]
df2=pd.DataFrame(data2,columns=['NAME','AGE'])
print (df2)

#appending one data frame with the other
df1=df1.append(df2)
print (df1.reset_index())

