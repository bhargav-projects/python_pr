
# '''A lot of times when dealing with iterators,
#  we also get a need to keep a count of iterations.
#   Python eases the programmers’ task by providing a built-in function enumerate()
#   for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# for only one line after FOR,ELSE,IF  we write statement directly

# for key,value in dict1.items():
#     if value not in result.values():result[key] = value
# #IN THIS    way u can write to FOR,ELSE,IF

# '''
# #copy method
# x={1:2}
# c={2:3}
#  #if we use 2 varibles it returns tuple of of objects
# d=c,x # here we can add multiple objects
# print(d)

# #C chainmap
# from collections import *
# s={1: 'hi', 2: 'BF'}
# b={4: 'i', 5: 'F'}
# a=ChainMap(s,b)  #returns tuple of dictionaries
# print(a)

# #E enumerate gives indexes of iterable items
# names='radha','krishna','guru','mahesh'
# # now it showing   ==>  0 radha
# for index,name in enumerate(names):
#     print(index,name)

# #with out index it showing output
# #like tuple values (0, 'radha')
# for name in enumerate(names):
#     print(name)

# #D Del key from user input
# d1={1:10,2:20,3:30,4:40,5:50}
# key=int(input("Enter key in range(1,5):-"))
# d1.pop(key)
# print(d1)


# d1={1:10,2:20,3:30,4:40,5:50}
# key=int(input("Enter key in range(1,5):-"))
# try:
#     d1.pop(key)
# except:
#     print("Wrong key")
# print(d1)


# d = {'a': 10, 'b':20, 'c':30}
# key = input("Enter Key:")
# if key in d:
#     del d[key]
#     print(d)
# else:print("Invalid key")


# #  removing Duplicates
# dict1={1:'a',2:'a',3:'b',4:'c',5:'c'}
# result = {}
# for key,value in dict1.items():
#     if value not in result.values():
#         result[key] = value
# print(result)

# #type2
# d={1:'hi',2:'no',3:'ok',4:'what next',6:'ok',5:'what next'}
# result=[]
# res=dict()
# for key,values in d.items():
#     if values not in result:
#         result.append(values)
#         res[key]=values
# print(res)

# temp={values:key for key,values in d.items()}
# res={values:key for key,values in temp.items()}

# #M MERGING DICT
# d1={1:2,2:3}
# d2={2:1,3:2}
# # it will show unique dictionary values , you can use this two objects
# print({**d1,**d2})

# #3.9.6 version on wards
# print(d1|d2)  # it can works with set too

# dic1,dic2,dic3={1:10},{3:30},{}
# for items in dic1,dic2:
#     dic3.update(items)
# print(dic3)

# #producting Dict
# from itertools import product
# d={'1':['a','b'],'2':['c','d']}
# for x,y in product(*d.values()):
#     print(x+y)

# d ={'1':['a','b'], '2':['c','d']}
# for x in d['1']:
#     for y in d['2']:
#         print(x + y)

# import itertools
# d ={'1':['p','q'], '2':['a','c']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))

# from itertools import product
# d={1:['a','b'],2:['c','d']}
# print(d)
# for k,v in product(*d.values()):
# 	print(k+v)


# d={'item':'foot','price':'10'}
# #if we use get when we dont initialise any keys with it gives none
# # count=d.get('hi')
# # #instead of none  we use our defined value
# # count=d.get('hi','hi value Not Found')

# '''
# if no value to setdefalut it give none value
# set defualt used to create a new key,value in dict object
# '''
# count=d.setdefault(4) #returns none value
# count=d.setdefault(4,'we given 4')
# print(d)


# import random
# lst =[]
# for i in range(5):
# 	x = random.randint(1,30)
# 	lst.append(x)
# print(lst)


# #print vowel in name
# word=input('enter words')
# vowels=('a','e','i','o','u',"A",'E',"I",'O','U')
# d={}
# for x in word:
#     if x in vowels:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print(k,'..',v)


# class student:
#     stu=list()
#     #this is for storing data to the list
#     def add():

#         d={'name':input('enter name'),'number':int(input('enter number'))}
#         student.stu.append(d)
#     def show():
#         key=input('enter student name u want')
#         flag=False
#         for i in student.stu:
#             if key==i['name']:
#                 flag=True
#                 print('student name',i['name'])
#                 print('student number',i['num'])
#         if not flag:
#             print("not found")
#     def delete():
#         key=input('enter stu name u want to delete')
#         flag=False
#         for i in student.stu:
#             if key==i['name']:
#                 flag=True
#                 student.stu.remove(i)
#         if not flag:
#             print("not found")

# student.add()

# ###
# class Student:
#     student_rn='101'
#     student_name='sita'

# print("to show the student details:")
# for key, value in Student.__dict__.items():
#     if not key.startswith('_'):
#         print(f'{key} -> {value}')


# #magic methods
# class student:
#     def __init__(self, name, rollno):
#         self.Name = name
#         self.Roll_No = rollno

#     def add(self, Name, Rollno ):
#         for i in range(4):
#             Name = input("Enter name:")
#             Rollno = int(input("Enter Roll no:"))

#             ob = student(Name, Rollno )
#             ls.append(ob)

#     def display(self, ob):
#             print("Name   : ", ob.Name)
#             print("RollNo : ", ob.Roll_No)

#     def remove(self):

#         del(self.Name )
#         del(self.Roll_No)
#         print('deleted student successfully')
# ls=[]
# s=student('',0)

# print("\n1.Add Student details\n2.Display Student Details\n3.Delete Details of Student")

# ch = int(input("Enter choice:"))
# if(ch == 1):
#     s.add('',0)
#     print("\nList of Students\n")
#     for i in range(ls.__len__()):
#         s.display(ls[i])

# elif(ch == 2):

#     print("\nList of Students\n")
#     for i in range(ls.__len__()):
#         s.display(ls[i])

# elif(ch == 3):
#     s.remove()
#     print(ls.__len__())
#     print("List after deletion")
#     for i in range(ls.__len__()):
#         s.display(ls[i])
# else:
#       print("Invalid choice")

 