#creating a text file via with ..context manager
import os,sys
with open('dsfile2.txt','w') as fo:
    print ('enter text')
    s=sys.stdin.read()
    fo.write(s)
