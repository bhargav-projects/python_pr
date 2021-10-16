'''
defduplicate=main()  #this is fun caLL 
defduplicate=main    #this is giving duplicate name
'''


from functools import reduce as re
def sub_sum(a, b):
    sum = a+b
    sub = a-b
    return a+b, a-b  # instead of this we can take sum,sub


x, y = sub_sum(10, 30)
print('sum=', x)
print('sub=', y)

# multiple returns


def sub_sum(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return a+b, a-b, mul, div  # instead of this we can take sum,sub


x, y, z, v = sub_sum(10, 30)
print('sum=', x)
print('sub=', y)
print('mul=', z)
print('div=', v)

# tuple packing


def sub_sum(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return a+b, a-b, mul, div  # instead of this we can take sum,sub=


t = sub_sum(10, 30)                    # packing in tuple concept
for x in t:
    print(x)

   
t=sub_sum(10,30)  # all values in single tuple format
print(t)

 

#Special Functions# 

#1 filter() function to filter values from the given sequence based on some condition. (even,odd)
#2 map() :For every element present in the given sequence,apply some functionality and generate (mu2 lists,mul)
# new element with the required modification. For this requirement we should go for 
#3 reduce():reduce() function reduces sequence of elements into a single element by applying the specified function.(sum,mul)


#3
l = [10, 203, 4, 204, 3023, 202]
# in the place of l u cAN take tup or str because that takes any sequence
l1 = list(map(lambda x: x*x, l))
print(l1)
l2 = list(filter(lambda x: x % 2 == 0, l))
print(l2)
l3 = list(filter(lambda x: x % 2 != 0, l))
print(l3)

# differents between map and without map
l1 = [10, 20, 30, 40]
l2 = [1, 2, 3, 4, 5]
l3 = [lambda x, y:x*y, l1, l2]
print(l3)

# when extra values
# if extra values there it ignores the values
l1 = [10, 20, 30, 40, 50, 60, 70]
l2 = [1, 2, 3, 4, 5]
l3 = list(map(lambda x, y: x*y, l1, l2))
print(l3)

# but map returns boolen value based on ur condition because not same length
#i fu try to check conditi it gives boolen values
l1 = [10, 20, 30, 43, 50]
l2 = [1, 2, 3, 4, 5]
l3 = list(map(lambda x: x % 2 == 0, l1))
print(l3)

# reduce : the given sequence or result will be form to one sngle value
# reduce function must import from functiontools
l1 = [10, 20, 30, 40, 50, 60, 70]
l3 = re(lambda x, y: x+y, l1)
print(l3)

# FUN INSIDE FUN OR NESTED FUN :

# type 1 (accessing  inner fun inside f1 fun by direct call)
def f1():
    def innerfun(a, b):
        print('the sum of a,b is:', a+b)
        print('the avg of a,b is :', (a+b)/2)

    innerfun(2, 3)
    innerfun(20, 5)
    innerfun(30, 6)
f1()

#type 2 (accessing inner fun in insdie  f1 using return )
def out():
    print('this is outer starting')
    #print('now outer function returning inner ')
    def inner():
        print('this is inNERer')
    print('now outer function returning inner ')
    return inner
out()  # it cant call inner fun bcoz there is no name  for  return  inner value
fun=out()# this decalration is for calling inner  fun from outside(fun is annother name we provided)  
fun()    # here is the callling of inner from outside 

# exmaple for TYPE2 1function can return another fun 
def f1():
    print('here we are calling directly by using outside fun return ')
    def f2(a,b):
        print('innerfunction',a+b)
    f2(2,3)
    return f2
f1() #f1 call 
                    
# ERROR
def f1():
    def innerfun(a,b):
        print('the sum of a,b is:', a+b)
        print('the avg of a,b is :', (a+b)/2)
f1()
# we cant call inner fun  outside of main fun  outside
#innerfun(2, 3)
#innerfun(20, 5)
#innerfun(30, 6)
#f1().inner(10, 20)


#decors concept
#TYPE1 
def decor(fnc): # decor function takes function as argument 
    def inner(name):
        if name=='bhargav':
            print('gd boy')
        else:
            fnc(name) # instead of  wish we must take dec function  i,e func 
    return inner

def wish(name):
    print('hi ',name,'bhargav')
    
decorfunction=decor(wish)
wish("bhargav") # normal calll
decorfunction('bhargav')

#TYPE1 EX2
def d(f):
    def im(name):
        if name=='d':

            print('this is decor')
        else:
            return f(name)
    return im

@d
def wish(name):
    print('hi ',name, 'this is not decor')

wish('bhargav')
wish('d')

#type 2
def decor(f):
    def im(name):
        if name=='d':

            print('this is decor')
        else:
            return f(name)
    return im


def wish(name):
    print('hi ',name, 'this is not decor')

decorfunction=decor(wish)
wish('bhargav')
# wish('d') this is also applicable 
decorfunction('d')

#type 2.1   no ned to type full name decor needs one varble thats it

def d(f): #this is decor 
    def im(name):
        if name=='d':

            print('this is decor')
        else:
            return f(name)
    return im

def wish(name):
    print('hi ',name, 'this is not decor')

d=d(wish)  # no ned to type full name decor needs one varble thats it
wish('bhargav')
# wish('d') this is also applicable 
d('d')

# zero div error display
def z(f):
    def im(a,b):    
        if b==0:
            print('we cant dvision with zero bro sorry ')
        else:
            return f(a,b)
    return im
@z # zerodivision decor
def div(a,b):
    print('the div of a,b is ',a/b)
    
div(3,4)
div(2,9)
div(3,0)

# *DECORATOR CHAINING
# default decor applied to existing fun
def d1(f1):
    def im(name):
        print('dec 1 ')
        return f1(name)
    return im

@d1
def main(name):
    print('this is  default  decor execution')
main('hi')

# EXAMPLE 2 MULTIPLE DEC
# default decor applied to existing fun
def d1(f1):
    def im(name):
        print('dec 1 execution ')
        return f1(name)
    return im
def d2(f1):
    def im(name):
        print('dec 2  execution')
        return f1(name)
    return im
@d2
@d1
def main(name):
    print('hi ',name,'this is  default  main execution')
# 2 dec wil execute for every call 
main('hi')
main('how')



#new method''magic of fun is it can evalute with their expresions with their arguments

def length(a,b):
    return a(b)
print(length(len,'abcdef'))  #" here len is inbuilt fun it takes one expression to evalute "

def length(a,b):
    return a(b)
print(length(sum,[1,2,3])) #" sum is inbuilt fun and but its argument of a , and given list is parameter of bth position"

#''' WE CAN ACCESS LOCAL VARIABLES BY ACCESSING THEIR RESPECTIVE CLASSES '''
from threading import *
import time
class custom1(Thread):
    res=0 #static
    def run(self):
        for i in range(1,default.n+1):
            custom1.res +=i   # HERE WE ADD CLASS AS WELL AS VAR AND MAKE NEW VARIABLE 
        return
class default:
    n=0
    def main():
        default.n=int(input('enter number '))   # HERE WE ADD CLASS AS WELL AS VAR AND MAKE NEW VARIABLE 
        o1=custom1()
        o1.start()
        
        o1.join()
        print(' res is:'+str(custom1.res))
        return
default.main()


