# a+ mode
import os, sys
with open('dsfile7.txt','a+') as fo:
    print ('enter more data to add ')
    s=sys.stdin.read()
    fo.write(s)
    fo.seek(0,0)
    t=fo.read()
    sys.stdout.write(t)
    
