# pie plotting using pandas Series
import pandas as pd
from matplotlib import pyplot as plt
fruits=['apples','pears','cherries','bananas']
quantity=[20,30,40,10]
s=pd.Series(quantity,index=fruits,name='series')
s.plot.pie(figsize=(6,6))
plt.show()


