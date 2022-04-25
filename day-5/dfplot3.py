# bar plotting using pandas
import pandas as pd
from matplotlib import pyplot as plt
data={'CITY':['LONDON','PARIS','ROME'],'VISITS':[20,40,12]}
df=pd.DataFrame(data)
print (df)

#bar plotting
df.plot.bar(x='CITY',y='VISITS',title='NO. OF VISITS PER YEAR')
plt.show()
