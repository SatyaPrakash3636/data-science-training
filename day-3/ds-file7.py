#displaying the file content
import os,sys
with open('dsfile1.txt','r') as fo:
        s=fo.read()
        sys.stdout.write(s)
        
    
