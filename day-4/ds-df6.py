#create a data frame from a dictionary of ndarrays/lists
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df= pd.DataFrame(data)
print (df)
