#storing lists and dictionaries in files - json module
import os,json
x=['computer','printer','scanner','monitor','technology']
with open('dsdata1','w') as fo:
    json.dump(x,fo)
    
y={'p':1,'q':'abc','r':[1,2,3],'s':(4,5,6),'t':{'a':1,'b':2}}
with open('dsdata2','w') as fo1:
    json.dump(y,fo1)
    
