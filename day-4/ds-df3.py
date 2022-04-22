#creating a data frame from a list
import pandas as pd
data=[('AAA',111),('BBB',222),('CCC',333)]
df1=pd.DataFrame(data,columns=['NAME','CODE'])
print (df1.to_string(index=False))
