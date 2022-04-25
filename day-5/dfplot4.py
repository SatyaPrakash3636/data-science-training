#read_excel
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_excel(r'c:\python39\myclass.xlsx',sheet_name='Sheet1')
df.plot.bar(x='CLASS',y='SNUMBER',title='YEAR DATA')
plt.show(block=True)

