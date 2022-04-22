#scattered graph

#import the libraries
from matplotlib import pyplot as plt
import numpy as np

#take axes coordinates
x=[1,3,5,7,9]
y=[11,22,33,44,55]

#draw the scattered plot
plt.scatter(x,y, color='red', marker='+')

#show
plt.show()
