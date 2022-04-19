#use of filter()
def f1(x):
    return x%2==0

z=filter(f1,[1,2,3,4,5,6,7,8,9])
print (list(z))

def f2(x):
    return x.isupper()

z=filter(f2,'HP ComputerS')
print (list(z))

def arm(n):
    s=n
    t=0
    while s!=0:
        r=s%10
        t+=r**3
        s//=10
    return n==t

z=filter(arm,range(100,1000))
print (list(z))

