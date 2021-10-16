#WAP TO count create no of objects in the class
class Test:
    count=0
    def __init__(self):
        Test.count+=1
    @classmethod
    def NoOfObjectsCreated(cls):  #we dont take self so we taken class 
        print('the no of obj created',Test.count)

t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.NoOfObjectsCreated()

#GC  garbage collector
#if we are working with large more of obj then enable is best otherwise performance will slow
import gc
print(gc.isenabled()) #true
gc.disable()
print(gc.isenabled()) #false
gc.enable()
print(gc.isenabled()) #true

#destroying objects 
class test:
    def __init__(self):
        print('this is class method')
    def  __del__(self):
        print(' the objects deleted')
list=[test(),test(),test()]
del list  # even though we are not using del but inside del consturctor wil executes
print('end of application')


#this is also destrcuting obj
#once the control reaches end of the program ,automatically all the objects elgible for gc
class test:
    def __init__(self):
        print('this is class method')
    def  __del__(self):
        print(' the objects deleted')
list=[test(),test(),test()]
print('end of application')

#WAP to count no of reference varible for currrent obj
import sys
class test:
    pass
t1=test()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))  #we get output 5 ,Because of for every obj will  python give one reference varibale   i.e, is self so. 5 reference varible total
# none means reference varible not pointing to any object but referancevarible is available
# varible=None  ; and none is also obj in python

