#copying a file via commandline arguments
import os,sys
with open(sys.argv[1],'r') as fo1, open(sys.argv[2],'w') as fo2:
    s=fo1.read()
    fo2.write(s)
    
