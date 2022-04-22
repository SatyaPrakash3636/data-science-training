#setting legends and limits for axes

#importing libraries
from matplotlib import pyplot as plt
import numpy as np

#set the coordinates for axes
x1=[1,3,5,7,9]
y1=[10,30,50,70,90]

x2=[2,4,6,8,10]
y2=[60,40,80,20,10]

#draw the graphs
g1,=plt.plot(x1,y1,'r')
g2,=plt.plot(x2,y2,'g')

#legends
plt.legend([g1,g2],["Q1","Q2"])

#labels
plt.xlabel("CODE")
plt.ylabel("QTT")

#limits
plt.xlim(1,10)
plt.ylim(10,100)

#display
plt.show()
        
