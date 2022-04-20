#create a text file from keyboard

#importing necessary modules
import os,sys

#create the file object
fo=open('dsfile1.txt','w')

#read data from keyboard into a string
print ('enter data ')
s=sys.stdin.read()

#write the string on to the file object
fo.write(s)

#close the file object
fo.close()
