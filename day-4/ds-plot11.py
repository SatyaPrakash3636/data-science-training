#pie chart

#import libraries
import numpy as np
from matplotlib import pyplot as plt

#pieces
activities=['eat','work','play','sleep']
slices=[15,50,10,25]
colors=['r','g','b','y']

#drawing the pie chart
#plt.pie(slices,labels=activities,colors=colors,explode=(0,0,0.5,0),autopct='%1.1f%%')
plt.pie(slices,labels=activities,colors=colors,explode=(0,0,0,0.2),autopct='%1.1f%%')

#show
plt.show()
