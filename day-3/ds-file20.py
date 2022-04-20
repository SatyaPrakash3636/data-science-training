#reading a csv file
import os,csv
with open('dscsv','r') as fo:
    y=csv.reader(fo)   #creating a reader object
    for m in y:
        print (m)
        
