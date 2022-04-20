#w+ mode
import os,sys
with open('dsfile7.txt','w+') as fo:
    print ('enter data')
    s=sys.stdin.read()
    fo.write(s)
    fo.seek(0,0)
    t=fo.read()
    print ('displaying entered data')
    sys.stdout.write(t)
    
