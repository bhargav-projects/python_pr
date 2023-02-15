"""
polymorphism: one name many forms
"""

'''
duck typing , Overloading, Overiding

Overloading: method, constructor, operator (Overloading)
Overriding: method & constructor Over riding
'''

'''
duck typing :
python give importance behaviour of object not type of object

'''
# duck typing
class Dog:
    def bark(self):
        print("bark")

class cat:
    def meow(self):
        print("meow")

def fun(obj):
    if hasattr(obj, "bark"):
        obj.bark()
    elif hasattr(obj, "meow"):
        obj.meow()

# d=Dog()
# fun(d) this is called duck typing , it follows behaviour not decleration

"""
Overloading
"""

class Student:
    
    def __init__(self,score):
        self.score = score
    # here we are overriding the existing add methods using magic methods
    # here self means current object , other means another objects
    def __add__(self,other): #magic methods 
        return self.score + other.score
    
    #more than two objects
    # def __add__(self,other): #magic methods
    #     total =  self.score + other.score
    #     return Student(total)

    def __mul__(self,other):
        return self.score * other.score

s1=Student(10) #if requirement is sum of different objects
s2=Student(20)
print("this is add ", s1+s2)
print("this is mul ", s1*s2)
s3=Student(30)
print(s1+s2+s3) #((s1+s2) + (s3))

#different objects of different class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __mul__(self,other):
        # here self means current object , other means another objects 
        return self.salary*other.days
        
class Timesheet:
    def __init__(self, days):
        self.days = days
        
e=Employee("bhargav",10000)
t=Timesheet(25)
print("Employee salary is ", e*t)
# print("Employee salary is ", t*e) #here it wont work bcz not defined mgc mtd in Timesheet object
