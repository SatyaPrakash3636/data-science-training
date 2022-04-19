#lambda
#normal function
def f1(x):
    return x**2

z=f1(10)
print (z)

#lambda example:1
s=lambda x: x**2
z=s(10)
print (z)


#lambda example:2
z=lambda x,y:x*y
r=z(10,12)
print (r)

#lambda example:3
r=lambda x:x**2 if x>12 else False
z1=r(10)
print (z1)
z2=r(20)
print (z2)

#lambda with map, filter
z=map(lambda x:x**2, [1,2,3,4])
print (list(z))

z1=filter(lambda x: x%2!=0, [1,2,3,4,5,6,7,8,9])
print (list(z1))



