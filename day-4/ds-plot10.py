#histogram

#import the libraries
import numpy as np
from matplotlib import pyplot as plt

#take the coordinates
ages=[2,5,70,40,30,45,46,43,44,40,60,47,13,17,34,21,57,18,80,77,32,36,67,54]
ranges=(0,80)
bins=10

#draw the histogram
plt.hist(ages,bins,ranges,color='yellow',histtype='step')
#plt.hist(ages,bins,ranges)

#display
plt.show()
