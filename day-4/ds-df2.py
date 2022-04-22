#creating a data frame from  a list
import pandas as pd
a=['computer','keyboard','monitor','printer','scanner']
a1=[('AAA',111),('BBB',222),('CCC',333)]
df=pd.DataFrame(a)
print (df)
df1=pd.DataFrame(a1)
print (df1)

