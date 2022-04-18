#for statement
n=input('enter a string in mixed case ')
lc=0
uc=0
dc=0
oc=0
for x in n:
    if x.islower():
        lc+=1
    elif x.isupper():
        uc+=1
    elif x.isdigit():
        dc+=1
    else:
        oc+=1
print ('%d lower, %d upper, %d digits, %d others' % (lc,uc,dc,oc))
