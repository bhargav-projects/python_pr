'''
defduplicate=main()  #this is fun caLL 
defduplicate=main    #this is giving duplicate name
'''

'''
Write a program to create
a function that will work like range function.
'''

import sys

def range_generator(start, stop, step):

    values = ''
    start = start-1

    while start < stop-step:  # while start value reaches the stop value

        value = start+step   # providing start value using start+step value
        values += str(value)
        start += step
    return ' '.join(values)


print(range_generator(5, 10, 2))

from functools import reduce as re
 
 
def sub_sum(a, b):
    sum = a+b
    sub = a-b
    return a+b, a-b

x, y = sub_sum(10, 30)
print('sum=', x)
print('sub=', y)

def sub_sum(a, b):
    return f"sum is {a+b}"

print(*sub_sum(10, 2))
 
#~Special Functions

"""
   #! for condition decleration ':' is not required for all
filter()-->Filter values from the given sequence based on condition
map()-->For every element present in the given sequence,apply some functionality 
reduce()-->Function reduces sequence of elements into a single elements.

"""

l = [10, 203, 4, 204, 3023, 202]
# map function to print odd and even numbers

l1 = list(map(lambda x: x%2==0, l)) 
even = []
odd = []
for index,val in enumerate(l1):
  if val == True:
    even.append(index)
  else:
    odd.append(index)
    
print(even,odd)
#^ In the place of list u can take tup or str because that takes any sequence
l1 = list(map(lambda x: x*x, l)) 
l2 = list(filter(lambda x: x % 2 == 0, l))

#^ IF You use any condition in map it return boolean values
l3 = list(map(lambda x: x % 2 == 0, l1))


from functools  import reduce as re
l1 = [10, 20, 30, 40, 50, 60, 70]
l3 = re(lambda x, y: x+y, l1) #280 <-- It SUM the each element with next element

 

#type 2 (accessing inner fun in insdie  f1 using return )
def out():
    print('this is outer starting')
    #print('now outer function returning inner ')
    def inner():
        print('this is inNERer')
    print('now outer function returning inner ')
    return inner   #^ This is called closures concept
out()  #! it cant call inner fun bcoz there is no name  for  return  inner value
#! this decalration is for calling inner  fun from outside(fun is annother name we provided)  
fun=out()
fun()    #^ here is the callling of inner from outside 

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
 
 



#new method''magic of fun is it can evalute with their expresions with their arguments

def length(a,b):
    return a(b)
    #" here len is inbuilt fun it takes one expression to evalute "
    
print(length(len,'abcdef'))  
def length(a,b):
    return a(b)
     #" sum is inbuilt fun and but its argument of a , and given list is parameter of bth position"
print(length(sum,[1,2,3]))

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


