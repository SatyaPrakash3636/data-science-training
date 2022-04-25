#plotting using pandas
import pandas as pd
from matplotlib import pyplot as plt
a={'CLASS':[1,2,3,4,5],'AGES':[7,6,5,8,4]}
df=pd.DataFrame(a)
print (df)

#plotting
df.plot(x='CLASS',y='AGES')
plt.show()
