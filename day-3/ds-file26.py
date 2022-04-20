#displaying a range of cells
from openpyxl import load_workbook
x=load_workbook('dsexcel2.xlsx')
y=x.active
cells=y['A1:C4']
for p,q,r in cells:
    print ('%-10s%-10s%-10s' % (p.value,q.value,r.value))

x.close()
