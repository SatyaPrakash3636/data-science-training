#line graph with labels

#import the libraries
import numpy as np
from matplotlib import pyplot as plt

#set the axes
classes=[1,2,3,4,5]
ages=[6,7,8,9,10]

#draw the graph
plt.plot(classes,ages)

#set the labels
plt.xlabel('CLASS')
plt.ylabel('AGE')

#display
plt.show()
