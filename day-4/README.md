# Table of Contents
**[1. DATA SCIENCE](#DATA-SCIENCE)**<br>
**[2. What is Pandas](#What-is-Pandas)**<br>
**[3. What are key features of Pandas?](#What-are-key-features-of-Pandas?)**<br>
**[4. What are important libraries for data science?](#What-are-important-libraries-for-data-science?)**<br>
**[5. Sample Examples](#Sample-Examples)**<br>
    - **[5.1 creating an empty data frame](#creating-an-empty-data-frame)**<br>
    - **[5.2 creating a data frame from  a list](#creating-a-data-frame-from-a-list)**<br>
    - **[5.3 creating a data frame from a list-1](#creating-a-data-frame-from-a-list-1)**<br>
    - **[5.4 create a data frame from a list thru input](#create-a-data-frame-from-a-list-thru-input)**<br>
    - **[5.5 create a data frame from a list with type float](#create-a-data-frame-from-a-list-with-type-float)**<br>
    - **[5.6 create a data frame from a dictionary of ndarrays/lists](#create-a-data-frame-from-a-dictionary-of-ndarrayslists)**<br>
    - **[5.7 create a data Frame from a dictionary of ndarrays/lists with index](#create-a-data-frame-from-a-dictionary-of-ndarrayslists-with-index)**<br>
    - **[5.8 create a data frame from a dictionary of series](#create-a-data-frame-from-a-dictionary-of-series)**<br>
    - **[5.9 row selection](#row-selection)**<br>
    - **[5.10 slicing the rows](#slicing-the-rows)**<br>
    - **[5.11 addition of  rows](#addition-of-rows)**<br>
    - **[5.12 appending one data frame with the other](#appending-one-data-frame-with-the-other)**<br>
    - **[5.13 column selection](#column-selection)**<br>

**[6. Plotting data on Graph](#plotting-data-on-graph)**<br>
    - **[6.1 line graph](#line-graph)**<br>
    - **[6.2 setting x and y axes for line graph](#setting-x-and-y-axes-for-line-graph)**<br>
    - **[6.3 line graph with labels](#line-graph-with-labels)**<br>
    - **[6.4 multiple line graphs](#multiple-line-graphs)**<br>
    - **[6.5 multiple line graphs with colors](#multiple-line-graphs-with-colors)**<br>
    - **[6.6 setting legends and limits for axes](#setting-legends-and-limits-for-axes)**<br>
    - **[6.7 line graph with markers](#line-graph-with-markers)**<br>
    - **[6.8 scattered graph](#scattered-graph)**<br>
    - **[6.9 creating a bar chart](#creating-a-bar-chart)**<br>
    - **[6.10 histogram](#histogram)**<br>
    - **[6.11 pie chart](#pie-chart)**<br>
    - **[6.12 Draw 2 plots](#draw-2-plots)**<br>
    - **[6.13 Draw 2 plots](#draw-6-plots)**<br>

## DATA SCIENCE:
    What is data science?
    Data Science is the field of analyzing and processing structured (formatted),
    and unstructured (unformatted, raw) data to generate valuable information
    through mathematical, statistical methods, AI & ML Algorithms.

### What is Pandas?
    Pandas is an open source Python library that provides high performance
    tools for data manipulation & processing.

    The name Pandas has come from 'Panel Data'

    Pandas data structures?
        1. series:
                one dimensional, homogeneous, immutable size
        2. data frame:
                two dimensional, heterogeneous, mutable size
        3. panel:
                three dimensional, heterogeneous, mutable size
        
### What are key features of Pandas?
        a. fast and efficient data frame philosophy
        b. tools for loading data from different file formats
        c. locating missing data
        d. row, column operations can be performed with great ease
        f. powerful merging and joining of data
        g. time series
        h. aggregation, grouping of rows and columns

### What are important libraries for data science?
        numpy (array operations)
        scipy (statistical operations)
        matplotlib (visualization)
        pandas (data analysis & processing)
        scikit-learn (machine learning)
        jupyter notebook (idle)

        
## Sample Examples

### creating an empty data frame
    ```python
    import pandas as pd
    df=pd.DataFrame()
    print (df)
    ```

### creating a data frame from  a list
    ```python
    import pandas as pd
    a=['computer','keyboard','monitor','printer','scanner']
    a1=[('AAA',111),('BBB',222),('CCC',333)]
    df=pd.DataFrame(a)
    print (df)
    df1=pd.DataFrame(a1)
    print (df1)
    ```

### creating a data frame from a list-1
    ```python
    import pandas as pd
    data=[('AAA',111),('BBB',222),('CCC',333)]
    df1=pd.DataFrame(data,columns=['NAME','CODE'])
    print (df1.to_string(index=False))
    ```

### create a data frame from a list thru input
    ```python
    #importing the libraries
    import pandas as pd

    #creating a list of ename and city tuples from keyboard
    data=[]
    ans='y'
    while ans=='y':
        ename=input('enter ename ')
        ecity=input('enter ecity ')
        m=(ename,ecity)
        data.append(m)
        ans=input('repeat (y/n) ')

    #store this data in a data frame
    df=pd.DataFrame(data,columns=['ENAME','ECITY'])
    print (df.to_string(index=False))
    ```

    
### create a data frame from a list with type float
    ```python
    import pandas as pd
    data = [['Alex',10],['Bob',12],['Clarke',13]]
    df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
    print (df)
    ```

### create a data frame from a dictionary of ndarrays/lists
    ```python
    import pandas as pd
    data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
    df= pd.DataFrame(data)
    print (df)
    ```

### create a data Frame from a dictionary of ndarrays/lists with index
    ```python
    import pandas as pd
    data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
    df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
    print (df)
    ```

### create a data frame from a dictionary of series
    ```python
    import pandas as pd
    d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)
    print (df)
    ```

### row selection
    ```python
    import pandas as pd
    data=[('AAA',111),('BBB',222),('CCC',333)]
    df=pd.DataFrame(data,columns=['NAME','AGE'],index=['first','second','third'])
    #total data frame
    print (df)

    #a column
    print (df['NAME'])

    #adding a new column
    df['CITY']=['hyd','chn','bnglr']
    print (df)

    #displaying row 2
    print (df.iloc[2])

    #displaying basing on index
    print (df.loc['second'])
    ```

### slicing the rows
    ```python
    import pandas as pd
    data=[('AAA',111),('BBB',222),('CCC',333)]
    df=pd.DataFrame(data,columns=['NAME','AGE'],index=['first','second','third'])
    #total data frame
    print (df)

    print (df[:1])
    ```

### addition of  rows
    ```python
    import pandas as pd
    #first data frame
    data1=[('AAA',111),('BBB',222),('CCC',333)]
    df1=pd.DataFrame(data1,columns=['NAME','AGE'])

    print (df1)
    print ()
    #second data frame
    data2=[('PPP',777),('QQQ',888),('RRR',999)]
    df2=pd.DataFrame(data2,columns=['NAME','AGE'])
    print (df2)
    ```

### appending one data frame with the other
    ```python
    df1=df1.append(df2)
    print (df1.reset_index())

    #joining the columns
    import pandas as pd
    #first data frame
    data1=[('AAA',111),('BBB',222),('CCC',333)]
    df1=pd.DataFrame(data1,columns=['NAME','AGE'])
    print (df1)
    print ()
    #second data frame
    data2=[('PPP',777),('QQQ',888),('RRR',999)]
    df2=pd.DataFrame(data2,columns=['CITY','PIN'])
    print (df2)

    #concatenating data frames
    df3=pd.concat([df1,df2],axis=1)
    print (df3)
    ```

### column selection
    ```python
    import pandas as pd
    data=[('AAA',111),('BBB',222),('CCC',333)]
    df=pd.DataFrame(data,columns=['NAME','AGE'])
    #total data frame
    print (df)

    #a column
    print (df['NAME'])

    #adding a new column
    df['CITY']=['hyd','chn','bnglr']
    print (df)

    #delete a column
    del (df['NAME'])
    print (df)

    #deleting a column
    df.pop('CITY')
    print (df)
    ```

# Plotting data on Graph

### line graph
    ```python
    #import necessary packages/modules
    import numpy as np
    from matplotlib import pyplot as plt

    #set the y-axis
    y=[3,7,9,11,6,8,4,2]

    #draw the line graph
    plt.plot(y)

    #display the graph
    plt.show()
    ```


### setting x and y axes for line graph
    ```python
    #importing the libraries
    import numpy as np
    from matplotlib import pyplot as plt

    #setting x and y axes
    x=[1,3,5,7,9]
    y=[15,17,19,21,13]

    #drawing the line graph
    plt.plot(x,y)

    #displaying
    plt.show()
    ```


### line graph with labels
    ```python
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
    ```


### multiple line graphs
    ```python
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
    ```

### multiple line graphs with colors
    ```python
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
    g1,=plt.plot(a,b,'r')
    g2,=plt.plot(c,d,'g')

    #label the axes
    plt.xlabel('id')
    plt.ylabel('age')

    #show
    plt.show()
    ```


### setting legends and limits for axes
    ```python
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
    ```
        
### line graph with markers
    ```python
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
    ```


### scattered graph
    ```python
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
    ```


### creating a bar chart
    ```python
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
    ```

### histogram
    ```python
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
    ```


### pie chart
    ```python
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
    ```


### Draw 2 plots
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    #plot 1:
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(2, 1, 1)
    plt.plot(x,y)

    #plot 2:
    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(2, 1, 2)
    plt.plot(x,y)

    plt.show()
    ```

### Draw 6 plots
```python
import matplotlib.pyplot as plt
import numpy as np
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()
```
