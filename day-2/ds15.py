#recursion
import os,sys
def mlt(num,level):
    if level<1:
        return
    else:
        mlt(num,level-1)
        print ('%d * %d = %d' % (num,level, num*level))

mlt(num=5, level=12)


def rev():
    p=sys.stdin.read(1)
    if p=='0':
        return
    else:
        rev()
        print(p,end=' ')

rev()
print ()

