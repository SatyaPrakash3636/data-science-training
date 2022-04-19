#aliasing
from dsmodule import f1 as ab,x
from dsmodule1 import abc,f1 as ac
print ('working with modules')
print ('calling module object')
ab()
ac()
print (x)

