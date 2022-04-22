#row selection
import pandas as pd
data=[('AAA',111),('BBB',222),('CCC',333)]
df=pd.DataFrame(data,columns=['NAME','AGE'],index=['first','second','third'])
#total data frame
print (df)

#a column
print (df['NAME'])

#adding a new column
df['CITY']=['hyd','chn','bnglr']
print (df)

#displaying row 2
print (df.iloc[2])

#displaying basing on index
print (df.loc['second'])





