#reading line by line - printing lower, upper alternately
import os,sys,time
with open('re.txt','r') as fo:
        k=0
        for m in fo:
            k+=1
            if k%2==0:
                m=m.upper()
            sys.stdout.write(m)
            time.sleep(1)
            
    
