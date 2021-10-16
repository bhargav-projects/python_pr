
'''A lot of times when dealing with iterators,
 we also get a need to keep a count of iterations.
  Python eases the programmers’ task by providing a built-in function enumerate() 
  for this task. 
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
for only one line after FOR,ELSE,IF  we write statement directly

for key,value in dict1.items():
    if value not in result.values():result[key] = value
#IN THIS    way u can write to FOR,ELSE,IF

'''
#copy method 
x={1:2}
c={2:3}
d=c,x.copy()  #if we use 2 varibles it returns tuple of dict and considered as tuple
print(d)  

#multiple objects copy but it returns tuple of dicts
x={1:2}
c={2:3}
e={3:4}
x1={1:2}
c1={2:3}
e1={3:4}
d=x1,c1,e1,e,c,x.copy()  #if we use 2 varibles it returns tuple of dict and considered as tuple
print(d[1])

#C chainmap
from collections import *
s={1: 'hi', 2: 'BF'}
b={4: 'i', 5: 'F'}
a=ChainMap(s,b)  #returns tuple of dictionaries
print(a)

#E enumerate gives indexes of iterable items
names='radha','krishna','guru','mahesh'
# now it showing   ==>  0 radha
for index,name in enumerate(names):
    print(index,name)

#with out index it showing output
#like tuple values (0, 'radha')
for name in enumerate(names):
    print(name)
    
#D Del key from user input 
d1={1:10,2:20,3:30,4:40,5:50}
key=int(input("Enter key in range(1,5):-"))
d1.pop(key)
print(d1)


d1={1:10,2:20,3:30,4:40,5:50}
key=int(input("Enter key in range(1,5):-"))
try:
    d1.pop(key)
except:
    print("Wrong key")
print(d1)


d = {'a': 10, 'b':20, 'c':30}
key = input("Enter Key:")
if key in d:       
    del d[key]
    print(d)
else:print("Invalid key")
    
    
#  removing Duplicates
dict1={1:'a',2:'a',3:'b',4:'c',5:'c'}
result = {}
for key,value in dict1.items():
    if value not in result.values():result[key] = value
print(result)

#type2
d={1:'hi',2:'no',3:'ok',4:'what next',6:'ok',5:'what next'}
result=[]
res=dict()
for key,values in d.items():
    if values not in result:
        result.append(values)
        res[key]=values
print(res)

#
temp={values:key for key,values in d.items()}
res={values:key for key,values in temp.items()} 

#F using for loop to get 
mydict={10:20,30:40}
print("type of accessing  dict value's using for loop")
for x in mydict.values():print(x)#
for k,v in mydict.items():print('keys.',k,'val.',v)
#if u want only keys
for keys in mydict:print(keys)

#M
#M MERGING DICT
d1={1:2,2:3}
d2={2:1,3:2}
#print({**d1,**d2}) 
print(d1|d2) #3.9.6 version on wards

dic1,dic2,dic3={1:10},{3:30},{}
for items in dic1,dic2:dic3.update(items)
print(dic3) 

d1,d2,d3={'A':1,'B':2,'C':3},{'D':4,'E':5,'F':7},d1.copy()
for key,value in d2.items():d3[key]=value
print(d3)

d1,d2,d = {1:"hello" , 2:"hi"},{3:"dd", 4:"sr"},{}
for k , v in d1.items():d[k]= v
for k,v in d2.items():d[k]=v
print(d)



#P
#P printing k,v separately
d={"hyd":32,"mumbai":34,"delhi":35,"kolkatha":30}
for i in d:
	print(i,d[i])  

dict1={'hyd':23,'knr':34,'sid':23,'sirc':40}
for i in dict1.keys():
    print(i,"...",dict1[i],'is','\u00b0C')

d = {"Delhi":50, "Mum":40 , "Hyd":43 ,"Bang":39}
print("city\ttemp")   # used tab it is escape character
for k,v in d.items(): # instead of d.items() we use d
	print("{}\t{}".format(k,v))

d={'Atp':35,'krn':45,'kdp':46,'vij':39}
for cities,temperatures in d.items():
    print(cities,':',temperatures)      

#producting Dict
from itertools import product
d={'1':['a','b'],'2':['c','d']}
for x,y in product(*d.values()):
    print(x+y)

d ={'1':['a','b'], '2':['c','d']}
for x in d['1']:
    for y in d['2']:
        print(x + y)

import itertools      
d ={'1':['p','q'], '2':['a','c']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
  
from itertools import product
d={1:['a','b'],2:['c','d']}
print(d)
for k,v in product(*d.values()):
	print(k+v)


d={'item':'foot','price':'10'}
# count=d.get('hi')  #if we use get when we dont initialise any keys with it gives none
# #instead of none  we use our defined value
# count=d.get('hi','hi value Not Found')
# print(d) #its not adding the get value to original d
 
#if no value to sdefalut it give none value
count=d.setdefault(4) #returns none value
count=d.setdefault(4,'we given 4')
print(d)

#dict comprehension
d = {x:x*x for x in range(20)}
print(d)

import random
lst =[]
for i in range(5):
	x = random.randint(1,30)
	lst.append(x)
print(lst)
 

#S square of number in dict
#for random values

#for one value
import random
random_num = random.randint(1,30)
print(f"Square of {random_num} is {random_num*random_num}")

#for range value
import random
for i in range(5):
    random_num = random.randint(1, 30)
    print(f"Square of {random_num} is {random_num*random_num}")

from random import randint
d={}
for i in range(1,10):
    value=randint(1,10)
    a=value**2
    d[value]=a
print(d)


#using while loop
n,d=10,{}
while n!=0:
  n=random.randint(1,10)
  d1[n]=n*n
  n-=1
print(d1)               

#for specified range
n,d=10,{}
for x in range(n+1):
    d[x]=x*x
print(d)

#using specified random squares range()  with no of times n
d1={}
for x in range(5): #instead of 5 u can use n for userdefined times
    i=random.randint(1,30)
    d1[i]=i*i
print(d1)

#sum values in dict
d1={1:10,2:20,3:30}
s=0
for i in d1:s+=d1[i]
print(s)

#individual element sum
d={1:10,2:20,3:30,4:40}
#by default it  prints only keys sum
print(sum(d),sum (d.keys()),end=' ')
# if use values it   gives values sum
print(sum(d.values()))
#type 3

def sum(d):
    sum=0
    for d2 in d:sum += d[d2]
    return sum
print(sum({'A':5,'B':10,'C':20,'D':55}))

#print vowel in name
word=input('enter words')
vowels=('a','e','i','o','u',"A",'E',"I",'O','U')
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,'..',v)
    

#storing student data 

#wap to store student name and detials in dict
rec,n={},2
while n!=0:
    name,num=input('enter student name'),int(input('enter student number'))
    rec[name]=num
    n-=1
for x in rec:
   print(f'{x} number is {rec[x]}')

class student:
    stu=list()
    #this is for storing data to the list 
    def add():
        
        d={'name':input('enter name'),'number':int(input('enter number'))}
        student.stu.append(d)
    def show():
        key=input('enter student name u want')
        flag=False
        for i in student.stu:
            if key==i['name']:
                flag=True
                print('student name',i['name'])
                print('student number',i['num'])
        if not flag:
            print("not found")
    def delete():
        key=input('enter stu name u want to delete')
        flag=False
        for i in student.stu:
            if key==i['name']:
                flag=True
                student.stu.remove(i)
        if not flag:
            print("not found")
            
student.add()

###
class Student:
    student_rn='101'
    student_name='sita'
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')


#magic methods
class student:
    def __init__(self, name, rollno):
        self.Name = name
        self.Roll_No = rollno
        
    def add(self, Name, Rollno ):
        for i in range(4):
            Name = input("Enter name:")        
            Rollno = int(input("Enter Roll no:"))       
            
            ob = student(Name, Rollno )
            ls.append(ob)
    
    def display(self, ob):
            print("Name   : ", ob.Name)
            print("RollNo : ", ob.Roll_No)
        
    def remove(self):
         
        del(self.Name )
        del(self.Roll_No)
        print('deleted student successfully')
ls=[]        
s=student('',0)

print("\n1.Add Student details\n2.Display Student Details\n3.Delete Details of Student")
    
ch = int(input("Enter choice:"))
if(ch == 1):
    s.add('',0)
    print("\nList of Students\n")
    for i in range(ls.__len__()):    
        s.display(ls[i])

elif(ch == 2):   

    print("\nList of Students\n")
    for i in range(ls.__len__()):    
        s.display(ls[i])
        
elif(ch == 3):
    s.remove()
    print(ls.__len__())
    print("List after deletion")
    for i in range(ls.__len__()):    
        s.display(ls[i])
else:
      print("Invalid choice")
             
