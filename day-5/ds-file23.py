#creating an excel file using python
'''
workbook => excel file
worksheet => active sheet
range => range of cells in the active sheet
cell => smallest data item
'''

from openpyxl import Workbook
x=Workbook()    #x is an object of Workbook class - create an excel file
y=x.active      #select the active sheet
y['A1']='computer'
y['B1']='printer'
y['C1']='scanner'
y['D1']=12345
x.save('dsexcel1.xlsx')
x.close()


