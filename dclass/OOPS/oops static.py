#TYPES  of declaring STATIC VARIBLE:
#1.inside class
#2 inside constructor
#3 inside instance method 
#4 inside method 
#5 inside static method 
#6 out side of the class  
class test:
    a=10           #normal static 
    def __init__(self): #constructor
        test.b=2
    def m1 (self):       # instance method 
        test.c=3
    @classmethod          # classmethod 
    def m2(cls):        # cls always  represent current class       
        test.d=4
        cls.e=5
    @staticmethod   #if we use static it is must be static and this is optional also
    def m3():
        test.f=6
t=test()
t.m1()
t.m2()
t.m3() 
test.g=3        #outside of the class
print(test.__dict__,t.g)


#if instance there it give first priority to instance
#and one more point always varible which declred finally is considered as latest value

class te:
    a=10
    def __init__(self):
        self.a=100
t=te()
print(t.a)
print(te.a)


# 
class test:
    a=10
    def m1 (self):
        self.a=888
t1=test()
t1.m1()
print(test.a)#there is no constructor so it give first priority to out side 

print(t1.a)  # we got instance variable so it  print inside value 

#
class test:
    x=10
    def __init__(self):
        self.y=20

t1=test()
t2=test()
print(t1.x,t1.y)
print(t2.x,t2.y)
t1.x=888
t1.y=999
print(t1.x,t1.y)
print(t2.x,t2.y)

#type 2 
class test:
    a=10
    def __init__(self):
        self.b=10
t1=test()
t2=test()
test.a=888
t1.b=999
print(t1.a,t1.b)
print(t2.a,t2.b)

# TYPE 4 
class test:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        self.a=888
        self.b=999
t1=test()
t2=test()
t1.m1()

print(t1.a,t1.b)
print(t2.a,t2.b)

#type 4
class test:
    a=10
    def __init__(self):
        self.b=20
    @classmethod
    def m1(cls):
        cls.a=888
        cls.b=999
t1=test()
t2=test()
t1.m1()
print(t1.a,t1.b)
print(t2.a,t2.b)
print(test.a,test.b)


class test:
    a=10
t=test()
print(t.a)
print(test.a) #
#but
#
class test:
    a=10
t=test()
t.a=20  #instance varible  still a=10 only
print(test.a)  #op =10
#we can acces static varible but we cant modify .if u want to modify use class name only
class test:
    a=10
t=test()
test.a=20  #instance varible  still a=10 onlt
print(test.a)
