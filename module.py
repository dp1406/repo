'''import time
from imp import reload
import module
time.sleep(10)
reload(module)
time.sleep(15)
reload(module)
print("this is test file")
print("this is from module")'''



'''x=10
y=20
def f1():
    print("Hello")
print(dir())
print()
x=888
def add(a,b):
    print("the sum of:",a+b)
def product(a,b):
    print("the product:",a*b)'''
def f1():
    if __name__=="__main__":
        print("the code executed as a program")
    else:
        print("the code executed as a module from some other program")
f1()





