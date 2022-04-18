#duck type programming
def fun1(x):
    for k,v in x.items():
        print (k,v)
    return

def fun2(y):
    y.append(100)
    print (y)
    return

def fun3(z):
    p=z.upper()
    print (p)
    return

fun1({'x':1,'y':2})
fun2([1,2,3,4])
fun3('computer')
