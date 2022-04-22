#column selection
import pandas as pd
data=[('AAA',111),('BBB',222),('CCC',333)]
df=pd.DataFrame(data,columns=['NAME','AGE'])
#total data frame
print (df)

#a column
print (df['NAME'])

#adding a new column
df['CITY']=['hyd','chn','bnglr']
print (df)

