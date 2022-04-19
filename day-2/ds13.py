#functions are first class objects
#assigning a function to an object
def f1():
    k=1
    while k<=3:
        print ('Python')
        k+=1
    return

m=f1
m()
print()
#putting the function as part of a list or dictionary
x=[1,'abc',f1,'pqr',[1,2,3]]
x[2]()
y={'a':123,'b':f1,'c':'abc'}
y['b']()

#passing functions to other functions, returning functions
def p(m,n):
    return m+n

def q(m,n):
    return m-n

def r(x,y):
    return x(12,10)+y(12,10)

z=r(p,q)
print (z)


