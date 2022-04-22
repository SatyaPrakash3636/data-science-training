#creating a bar chart

#import the libraries
import numpy as np
from matplotlib import pyplot as plt

#axes coordinates
left=[1,2,3,4,5]
heights=[10,24,36,20,15]

#bar naming
names=['JAN','FEB','MAR','APR','MAY']
colors=['blue','green','red','black','cyan']
#drawing the bar graph
plt.bar(left,heights,tick_label=names, color=colors)

#setting the labels
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')

#setting the title
plt.title('BAR CHART')

#displaying the graph
plt.show()
