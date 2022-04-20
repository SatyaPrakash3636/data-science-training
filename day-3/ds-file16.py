#other than text files
import os,sys
with open('x.exe','rb') as fo1, open('x11.exe','wb') as fo2:
    s=fo1.read()
    fo2.write(s)
    
