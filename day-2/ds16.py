#function inside function
def f1():
    print ('this is outside function')
    def f2():
        print ('this is inside function')
        return
    f2()
    return

f1()
