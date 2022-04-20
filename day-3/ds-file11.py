#count the pattern
import os,sys,re
with open('re1.txt','r') as fo:
    lc=0
    uc=0
    dc=0
    cc=0
    ec=0
    for m in fo:
        if re.search('^[a-z]+',m):
            lc+=1
        elif re.search('^[A-Z]+',m):
            uc+=1
        elif re.search('^[0-9]+',m):
            dc+=1
        elif re.search('^#',m):
            cc+=1
        elif re.search('^$',m):
            ec+=1
    print ('%d lower, %d upper, %d digit, %d empty, %d comment' % (lc,uc,dc,ec,cc))

            
