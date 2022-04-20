#remove the lines containing the word - python, Python or PYTHON
import os,sys,time,re
with open('re.txt','r') as fo1, open('result.txt','w') as fo2:
    for m in fo1:
        z=re.search('python|Python',m)
        if not z:
            fo2.write(m)

os.replace('result.txt','re.txt')
    
