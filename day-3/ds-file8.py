#reading line by line
import os,sys,time
with open('dsfile1.txt','r') as fo:
        for m in fo:
            sys.stdout.write(m)
            time.sleep(1)
            
    
