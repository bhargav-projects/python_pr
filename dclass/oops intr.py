
'''
#declare out side of the class is called function
#declare in side of the class is called  method
#help(doc) is also available 
#s=doc()  here s is the reference variable 
adv of reference var  is perform any operation inside obj
Actually RfrnceVrbl outside the class it access only outside class argu but
Within the class if u want to refer current obj we must 
req one referncvrbl,that variable is called SELF
'finally outside RfrVble and self both are referring same object'
'''
# reading doc  string in class types
# *type 1
class Student:
    '''hi this is doc string inside class '''  #always doc method in firstposition
print(Student.__doc__)
# help(Student)

# *type 2 (calling using  methods )
class Student:
    def hi():
        '''hi this is bhargav'''
s1 = Student()
print(s1.hi.__doc__)

# self is reference variable pointing to current object
# recommended method
class Student:
    def __init__(self):
        self.name = 'bhargav'
        self.no = 1
        self.sub = 'eng'

    def talk(self):  # we must declare self outside of constructor
        print(self.name)
        print(self.no)
        print(self.sub)


s = Student()  # here we are not using obj values  inside student obj
print(s.name)
s.talk()

# INSTEAD OF SELF U CAN DEFINE
# UR OWN NAME BUT IT MUST BE AFTER INIT
# because self is not reserved word  and its not keyword also
# Compulsory u must Declare any word because it is internally
# treated as current object reference and python will give default value for that


class S:
    def __init__(s):  #here instead of self i  declared my own variable 's'
        s.name = 'tracar'
        s.marks = 1001
        s.number = 1

    def dis(s):
        print('my name is ', s.name)
        print('my marks are ', s.marks)
        print('my number is ', s.number)


o = S()  # this line is called creating object and 'o' is the reference variable for that current created obj
o.dis()
print(o.__dict__)  # dict will give all data inside class in the form of key,value type

# by creating an multiple objects for single class
# recommedned method (for good progming practice we use self )
class Student:
    def __init__(self, x, y, z):  # x,y,z are object related varibles
        self.name = x  # self.name is instance variables
        self.no = y
        self.sub = z
        print(id(self))  #this adress and final s adress vlaues both are same

    def talk(self):
        print(self.name)
        print(self.no)
        print(self.sub)
        print(id(self))   # this self and talk self both are same
        print()           # here print beacause we get some clarity for previous output
    def meet(self):
        print(self.name)
        print(self.no)
        print(self.sub)
        print(id(self))   #this self and talk self both are same

s = Student('bha', 3, 1571)
e = Student('bhargav', 34, 1571)
e.talk()
e.meet()
print(id(s))            #this adress and final constructor self adress vlaues both are same

# here im taking different obj so self value is also changed for every obj change
#calling constructor explicitly
class checkinginit:
    def __init__(self):
        print('constructor execution')
        print(id(self))
t=checkinginit()
t.__init__()
s=checkinginit()
s.__init__()

#here im taking different arguments so self value is same but it accepts high argument value for all obj
class checkinginit:
    def __init__(self,x):
        print('constructor execution')
        print(id(self))
t=checkinginit(10)
t.__init__(100)
t.__init__(1040)

#ways of declaring instance varibles 
class test:
    def __init__(self):
        self.a=10
    def m1(self):
        self.b=20
o=test()
print(o.__dict__) #here only init will execute because
# we are not calling ,methods'
#type 2declaring instance varible 
o.m1()
print(o.__dict__) #now both values we will get
#type 3 declaring instance varibles
o.c=10

#new type 
#declaring class obj inside list

#list fun in main fun
class Movie:
    def __init__(self,Mname,hero,heroin,cost):
        self.Mname=Mname
        self.hero=hero
        self.heroin=heroin
        self.cost=cost
    def info(self):
        print('movie name ',self.Mname)
        print('hero name ',self.hero)
        print('heroin name ',self.heroin)
        print('ticket cost  ',self.cost)
        print()
movies=[Movie('little krishna','krishna','radharani',3.14 ),
        Movie('bhagvagitha','vasudeva','rukmini',9)
         ]    
for movie in movies:
    movie.info()

#oops NESTED CLASS ################################
class outer:
    def __init__(self):
        print('this is outer')
    class inner2:
        def __init__(self):
            print('this is inner2')
        class inner3:
            def __init__(self):
                print('inner 3')
            def m1(self):
                print('inner 3 m1')
#note compulsory inner class must be one tab space after outer class

#type1 innner3 m1()
t=outer()
t1=t.inner2()
t2=t1.inner3()  
# or 
t3=t1.inner3().m1()

#or simply 
#type 2 of accesing inner 3 m1()
outer().inner2().inner3().m1() 

#use of *has-A and is-A* relation ship is code reusability       
#composition  Method  (HAS-A relation)
#simply use class functionality i dont want to  extend the class functionlaity so has-A relation
class Engine:
    a=5
    def __init__(self):
        self.b=10
    def m1(self):
        print('this is engine functionality')
class car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('class car using engine car functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=car()
c.m2()
 
#declaring class as an argument in inside class 
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def carinfo(self):
        print('\tcar name',self.name)
        print('\tcar model',self.model)
        print('\tcar color ',self.color)
class emp:
    def __init__(self,name,number,sal,car): 
        self.name=name
        self.number=number
        self.sal=sal
        self.car=car #here we declaring car class as an argument
    def info(self):
        print('emp name ',self.name)
        print('emp number',self.number)
        print('emp salary',self.sal)
        print()
        print('car info')
        self.car.carinfo()
car=Car('toyota','100','yellow') #here we declaring car clas asa an argument
em=emp('bhargav','10','1000',car)  #here we declaring car clas asa an argument
em.info()

#using super class (is-A relation -INHERitance)
#if u want to extend the functionality of previous class then go for is-A realtion
class person:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def personinfo(self):
        print('hi bro how are you')
class emp(person):
    def __init__(self,name,num,sal):
        super().__init__(name,num) #observer here we are not using self here insdide SUPER() FUN in  inside the class
        self.sal=sal
    def info(self):
        print('emp name',self.name)
        print('emp number',self.num)
        print('emp salary',self.sal)
em=emp('bhargav','10','1000')  #here we declaring car clas asa an argument
em.personinfo()
em.info()

#has-A relation
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def carinfo(self):
        print('\tthis is car info')
        print('\tcar name',self.name)
        print('\tcar model',self.model)
        print('\tcar color ',self.color)
class person:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def personinfo(self):
        print('thi is person class ')
class emp(person):
    def __init__(self,name,num,sal,car):
        super().__init__(name,num) #observer here we are not using self here insdide SUPER() FUN in  inside the class
        self.sal=sal
        self.car=car
    def info(self):
        print('emp name',self.name)
        print('emp number',self.num)
        print('emp salary',self.sal)
        print()
        self.car.carinfo()

car=Car('toyota','100','yellow') #here we declaring car clas asa an argument
em=emp('bhargav','10','1000',car)  #here we declaring car clas asa an argument
em.personinfo()
em.info()
