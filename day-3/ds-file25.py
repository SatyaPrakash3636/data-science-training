#csv to excel
import os,csv
from openpyxl import Workbook
p=Workbook()
q=p.active
with open('dscsv','r') as fo:
    x=csv.reader(fo)
    for m in x:    #iterating thru the reader object (each line is got)
        q.append(m) #adding to the active sheet of the excel file
p.save('dsexcel2.xlsx')
p.close()

       

        
