#Instance method can call other instance method 
#Method with consists self called instance methods but own in own class 
#getter(accessor) and setter(mutator) method we always going to use instance varibles
#setter methods are alterantives for constructors 
#we dont no data in the begning later we want to add so we use this concept (s&g) concept

class test:
    #this is not class method because not using @class decorator to the method
    def m1(cls):   #this is instance method because python will give default value
        print('is this clas or static method')
        print(id(cls))
t=test()
#test.m1() #this is static method
t.m1()   # if we call like this is instance method 
print(id(t))

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):  #if it is from other class then it is static
        print('hi',self.name)  #because of self this method is called instance method 
        print('your marks are',self.marks)
s=student('Bhargav',100)
s.display()


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hi',self.name)  #because of self this method is called instance method 
        print('your marks are',self.marks)
    def grade(self):
        if self.marks>60:
            print('you got first rank')
        elif self.marks>50:
            print('you got second rank')
        elif self.marks>35:
            print('you got second rank')
        else:
            print(' you are failed')
        
    
s=student('Bhargav',100)
s.display()
s.grade()

#accessing outside instance method 
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hi',self.name)  #because of self this method is called instance method 
        print('your marks are',self.marks)
 #accessing outside fun and instance method 
        self.grade() 

    def grade(self):
        if self.marks>60:
            print('you got first rank')
        elif self.marks>50:
            print('you got second rank')
        elif self.marks>35:
            print('you got second rank')
        else:
            print(' you are failed')
s=student('Bhargav',100)
s.display()
#s.grade()


# I tried this but this is not recommended
#calling all methods is not gd programming practise based on 
#our requirements we need to call methods
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        # i tried this & is not recommended
        self.display()
        self.grade()  #accesing outside instance method 

    def display(self):
        print('hi',self.name)  #because of self this method is called instance method 
        print('your marks are',self.marks)
        

    def grade(self):
        if self.marks>60:
            print('you got first rank')
        elif self.marks>50:
            print('you got second rank')
        elif self.marks>35:
            print('you got second rank')
        else:
            print(' you are failed')
        
s=student('Bhargav',100)
#s.display()
#s.grade()


class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
l=[]
n=int(input('enter no of students '))
for k in range(n):
    s=student()
    name=input('enter name of the student')
    marks=int(input(' enter marks of the student'))
    s.setname(name)
    s.setmarks(marks)
    l.append(s)
print() # this is for gap 
for s in l:
    print('student name is ',s.getname())
    print('student name is ',s.getmarks())
    print()


#CLASS METHOD (only static varible usage methods are called)
#if we are not using any instance varible  we r using only static varible is called class method 
class Animal:
    legs=4
    @classmethod  # this @classmethod is compulsory
    def walk(cls,name):
        print('{} walks with{}'.format(name,cls.legs))
Animal.walk('dog')
t=Animal() 
t.walk('cat')

class test:
    def m1(cls):   #even though u are using cls it is nt clas method because u r nt declaring @classmethod
        print('is this clas or static method')

test.m1(10)


#STATIC METHOD==(General utility methods) add,division,...
#if we r nt using any instance or staticvariables  only using normal utility methods is called static methods
#adv are:  esssentially static methods let us write procedural code in object oriented language
#  It lets you call methods without having to create an object first 
#the only one time you want to use SM in a class is :-when given method does not require an instance of class to be created
class math:
      #it is optional
    def add(x,y):
        print('the sum is ',x+y)
    def sub(x,y):
        print('the sum is ',x-y)
    def div(x,y):
        print('the sum is ',x*y)
math.add(10,2)
math.sub(10,2)
math.div(10,2)
 
def m1(cls):
    print('this  is based on ur call ')
test.m1() # this is static method
t.m1() # this is instancce method  