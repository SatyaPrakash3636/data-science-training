#line graph with markers

#importing libraries
import numpy as np
from matplotlib import pyplot as plt

#coordinates for line-1
a=[3,6,5,4,7]
b=[13,29,15,11,19]

#drawing  lines
g1,=plt.plot(a,b,color='green',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)

#creating legends
plt.legend([g1,],["Q1",])

#lables
plt.xlabel('id')
plt.ylabel('age')

#setting the limits
plt.xlim(1,10)
plt.ylim(10,30)

#setting the title of the graph
plt.title('Q1 results of XYZ COMPANY')

#display the graph
plt.show()


