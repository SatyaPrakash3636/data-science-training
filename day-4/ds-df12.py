#slicing the rows
import pandas as pd
data=[('AAA',111),('BBB',222),('CCC',333)]
df=pd.DataFrame(data,columns=['NAME','AGE'],index=['first','second','third'])
#total data frame
print (df)

print (df[:1])
