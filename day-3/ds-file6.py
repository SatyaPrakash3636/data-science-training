#copying a file interactively via list
import os,sys
m=input('enter source file name ...')
n=input('enter target file name ...')
with open(m,'r') as fo1, open(n,'w') as fo2:
    p=fo1.readlines()
    print (p)
    fo2.writelines(p)
    
