#multiple line graphs

#import statements
from matplotlib import pyplot as plt
import numpy as np

#set the axes for line-1
x=np.array([1,3,5,7,9])
y=np.array([21,17,19,15,13])

#set the axes for line-2
x1=np.array([1,5,9,11,13])
y1=np.array([1,2,3,4,5])

#draw the plots
g1,=plt.plot(x,y,'r')
g2,=plt.plot(x1,y1,'g')

#label the axes
plt.xlabel('id')
plt.ylabel('age')

#show
plt.show()
