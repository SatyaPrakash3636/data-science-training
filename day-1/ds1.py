# compute net salary
basic=float(input('enter basic salary .. '))
hra=.4*basic
da=.2*basic
gross=(basic+hra+da)
ded=.1*gross
net=(gross-ded)
'''
print ('basic = %.2f  hra = %.2f   da = %.2f' % (basic, hra,da))
print ('gross = %.2f  ded = %.2f  net = %.2f' % (gross, ded,net))
'''
print ('basic = {0:.2f}   hra = {1:.2f}    da = {2:.2f}'.format(basic,hra,da))
print ('gross = {0:.2f}   ded = {1:.2f}   net = {2:.2f}'.format (gross, ded,net))


