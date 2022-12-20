'''
in set,tuple  update is used for instead of append (s.update(l))
#* inthese update we can add all type of elements and any no.of arguments 
#*but in update we cant pas int values separately
 but we can remove specific element by using s.remove(value)
 #*discord() tells if there is no element it dont show error
 #update() cant take int and float ,all arguments should be iterable objects.
 #add() takes any type of format ,add individual item to the Set
 We can use add() to ,where as we can use update() function 
#* symmetric difference means excluding common values 
set comprehension is also there 
s={} treated as empty dict
l=eval(input('enter l of values'))  it takes user defined data format
 like (2,3) or [2,3] or 23 or 'hi'
'''
# SET DOESNT SUPPORT INDEXING LIKE set[0]
# set Stores only imutable objects or immutable iterables not iterables 
set_ = {1,2 ,(3,4),"bhargav",range(10)} # executes
set_wont_save = {1,2,[3,4],{6,7},{9:10}} # throw error
# set_.update(10) # throw error but set_.update('abc') wont throw
 

#for detailed way  
l=[1,2,3,4,5,6,5,4,4,5,4]
x=set(l)    # this is creating set object
# it sorted after removing duplicates from list 
#sorted is inbuilt method
print(sorted(set(l))) 

s={1,2}
s.add(10)   
# we can add any dataformat but only one set of arguments by overcome this we use update()
s.add(10,20,3)  # TypeError: set.add() takes exactly one argument (3 given) 
# overcome error by = s.add((1,2,3)) or s.add(((1,2),(2,3))) 
s.add(((1,2),(2,3)))
print('add',s)

#update   (cons: update cant take int and float  as an argument) it takes str only
l=[12,13]
#s.update(l,range(10),'chakri',10) it gives error because of int(10)
s.update(10) # throws error single int elemetn we cant store in set
s.update(l,'chakri','10',range(10))
print('update',s)

#copy
s1=s.copy()
print('copy',s1)

#pop remove element in set and retrun that s.pop()
#remove(x) it removes particular element and only element at time
#discord(x) it wont give error if ele not available  reamaining functionality is same
#clear() clear all ele but and its like empty object

#UNION()  or  X|Y
s={1,2,3}
s1={2,3}
print(s.union(s1))

#intersection() or X&Y
#difference()   or x-y
#x.symmetric_difference(y) or x^y
#Returns elements present in either x or y but not in both

#vowels in word
w=input("Enter word to search for vowels: ") 
s=set(w) 
v={'a','e','i','o','u'} 
d=s.intersection(v) 
print("The different vowel present in",w,"are",d) 

#common ele in both sets
s,s_,s1=[1,2,3],{1,2},set()
for k in s:
    if k in s_:
        s1.add(k)
print('common ele are',s1)

#
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
list1=[]
for i in set1:
  for j in set2:
    if i==j:
      list1.append(j)
print(list1)     

#
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

#
def Number():
    list=[]
    for i in set1:
        for j in set2:
             return
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70} 
print(set1.intersection(set2))
Number()

#
set1={'abc','def','ghi'}
set2={'abc','jkl','mno'}
set3={'abc','mno','klm'}
print([x for x in set1 if x in set2 if x in set3]) 

#op=list of set 
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print([x for x in set1 if x in set2])

#
s1,s,s3={1,2,3,4},{2,3},[]
for x in s1:
        if x  in s:
                s3.append(x)
print('common ele in both the sets are',s3)

#min and max in set
s1={-55,2,3,4,7,8,386587}
l=list(s1)
mi,mx=l[0],l[0]
for i in l:
        if i >mx:
                mx=i
        if i<mi:
                mi=i
print(mi,mx)

#
s1={2,3,4,5,2,9}
l=list(s1)
mi=l[0]
ma=l[0]
for i in l:
    if i < mi:
        mi=i
    else:
	    ma=i
print('max is',ma,'min is',mi)
#
def max_check(x):
  max_val = x[0]
  for value in x:
    if value > max_val:
      max_val = value
  return max_val

def min_check(x):
  min_val = x[0]
  for value in x:
    if value < min_val:
      min_val = value
  return min_val

set = {15,56,1,254,995,32}
my_list =list(set)

print("Maximum of the Set : ", max_check(my_list))
print("Minimum of the Set : ", min_check(my_list))


#
set1={1,2,3,4,5}
t=0
w=0
min1=set ()
max1=set ()
for i in set1:
  if t>i:
    t=i
  elif w<i:
    w=i
min1.add(t)
max1.add(w)

print('{} is minimum value and {} is maximum value in set'.format(min1,max1))

#Write a program that will find all the unique string  values from 3 sets
#Unique values in str (neglecting duplicates)
#compare with 3 sets
s1,s2,s3,s= {'a','b','c','d'},{'c','e','f','a'},{'g','c','p','a'},set()
for i in s1:
    if i not in s2 and i not in s3:
        s.add(i)
for i in s2:
    if i not in s1 and i not in s3:
        s.add(i)
for i in s3:
    if i not in s2 and i not in s1:
        s.add(i)
print(s)
  #comparing set1 with two sets
s1,s2,s3,s= {'a','b','c','d'},{'c','e','f','a'},{'c','p','a'},set()
for i in s1:
    if i not in s2:
        if i not in s3:
            s.add(i)
print(s)
#R Remove duplicates in set int values
set1={10,20,30,40,50}
set2={30,40,50,60,70}
set3={60,70,80,90}
print(set1^set2^set3)


#eRRor 
print([('common elements',x) for x in {10, 20, 30,} if x in {30, 60, 70}])