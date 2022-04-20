#file modification
import os,sys
with open('re.txt','r+') as fo:
    #file stream object position
    print ('file opening %d' % fo.tell())
    #read first 25 characters
    s=fo.read(25)
    t=s.upper()
    print ('file stream after 25 chars read  %d' % (fo.tell()))
    #moving to the file beginning
    '''
    fo.seek(12,0)      #2nd - 0 file begin, 1 current pos, 2 file end
    fo.seek(12,1)
    fo.seek(-12,2)
    '''
    fo.seek(0,0)
    fo.write(t)
    
