#file object attributes
import os,sys
with open('re.txt') as fo:
    print ('name of the file is ', fo.name)
    print ('mode of the file is ', fo.mode)
    print ('the file is closed ', fo.closed)
    print ('file descriptor is ', fo.fileno())
    fo.flush()
print ('the file is closed ', fo.closed)

