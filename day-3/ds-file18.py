#retrieving list or dictionary from a file - json module
import os,json
with open('dsdata1','r') as fo:
    x=json.load(fo)
    print (x)

with open('dsdata2','r') as fo1:
    y=json.load(fo1)
    for k,v in y.items():
        print (k,v)
        
