#passing args and returning values
import os
def fun1(fname, fext):
    r=fname+'.'+fext
    return(r, os.path.getsize(r))

print ('passing filename and file extension as arguments ')
z=fun1('ds1','py')
print (z)


