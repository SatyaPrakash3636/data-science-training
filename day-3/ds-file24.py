#reading an excel file using python
'''
workbook => excel file
worksheet => active sheet
range => range of cells in the active sheet
cell => smallest data item
'''

from openpyxl import load_workbook
x=load_workbook('dsexcel1.xlsx')
y=x.active
p=y['A1'].value
q=y['B1'].value
r=y['C1'].value
s=y['D1'].value
print (p)
print (q)
print (r)
print (s)
