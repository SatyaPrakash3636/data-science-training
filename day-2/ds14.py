#local and global variables
def f1():
    k=222  #local k
    print ('inside the function ', k)
    global m
    m=k+globals()['k']
    print (m)
    return
k=111
print ('before the function ', k)
f1()
print ('outside the function ', k)
print (m)

