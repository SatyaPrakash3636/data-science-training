#use of map
def f1(x):
    return x**2

z=map(f1,[1,2,3,4,5])
print (z)
r=list(z)
print (r)

def f2(x,y):
    return x*y

z=map(f2,[1,2,3,4],[5,6,7,8])
print (type(z))
print (list(z))

def f3(x,y,z):
    return x+y+z

z=map(f3,'printer','monitor','scanner')
print (list(z))
