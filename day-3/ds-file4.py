#copying a file interactively
import os,sys
m=input('enter source file name ...')
n=input('enter target file name ...')
with open(m,'r') as fo1, open(n,'w') as fo2:
    s=fo1.read()
    fo2.write(s)
    
