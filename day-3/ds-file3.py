#copying a file
import os,sys
with open('dsfile2.txt','r') as fo1, open('dsfile3.txt','w') as fo2:
    s=fo1.read()
    fo2.write(s)
    
