''' len() is only applicable for lst,tuple,set,str,dict,range OR  sequence items
except =int complex bool
sorted(),reversed(),count(), these fun always give list format 
In list we have sort() fun but not in tuple so in tuple we use sorted()
In sorted (reverse=True ) for values in reverse and descending order
#*  we can pack list tuple set dict str
We can use + and * operators for List objects

'''
# It is returning list of str output
s="Learning Python is very very easy !!!" 
print(type(s)) 
l=s.split()  # it is returning list of str output
print(l) 
print(type(l)) 
# solve index out of range error using membership operators
l=[1,2,3,4,5,6,11,8,9,0]
l1=[10,20,30,40,50]
target=int(input('enter number to search'))
if target in l:
    print(target,'available at first occurence',l.index(target))
else:
    print(target ,'is not available')

print(l.append(10)) # directly add elemts to end
print(l.insert(2,10)) # add at specified index 
print(l.insert(100,1000)) # if index out of range it add elements to end if it is +Ve vale
print(l.insert(-10,100))  # if index less than zero it add elements to front position
print(l.append(l1))   # u can append all values And append fun takes only one argument
print(l.remove(9))  #  we cant remove use with index  # if no value it give Value Error
print(l.pop()) # if len(l) > than list then pop will executes otherwise give error
print(l.pop(7)) #  using with index not  index values # if no values there in lst  it give Index Error
print(l)
print(l.clear()) # it will clear everything and shows empty list 

#reversing list lements
l=[1,2,3,4,5,6]
newlist=[]
while l:
    temp=l.pop()
    newlist.append(temp)
print(newlist)

#printing list into row and matrix style 
x=[[10,20,30],[40,50,60],[70,80,90]]
print('elements row wise ')
for r in x :
    print(r)
print('elements in matrxi style')
for k in range(len(x)):
    for j in range(len(x[k])):
        print(x[k][j],end=' ')
    print()

#lst comprehension for squares range (10)
l=[]
for x in range(1,11):
    l.append(x*x)
print(l)

#lst comprehension
l1=[x**2 for x in range (10)  if (x**2)%2==0]
print(l1)

#for squares
print(list(map(lambda x:x*2,[1,2,3])))
#in place of list u take tup,se,dic,
##in place og [1,23] u take {1,2,3},(1,2,3)

#word programs 
words=['krishna','radharani']
l=[w[0] for w in words ]
#l=[w[0+len(words)] for w in words ]
print(l)

# words contain only more than 6 chars 
words=['krishna','radharani','bhar']
l=[w for w in words if  len(w)>6]  # words contain only more than 6 chars 
print(l)

# p to elements of x not in anthoer lst 
n1=[10,20,30,40]
n2=[30,40,50,60]
n3=[x for x in n1 if x not in n2 ]
print(n3)

words='hi bhargav how r u'
l=[[w.upper(),len(w)] for w in words ]
print(l)


# we can pack list tuple set dict str
a=10
b=20
c=30
l=[a,b,c]
print(l)

#unpacking
t=[10, 20, 30]
a,b,c=t
print(a,b,c)

#converted to single list
a=[[10,20,30],[30,40,50],[50,60,70]]
b=[y for x in a for y in x] # Y for X in a Y in X
print(b)

a=[]
while True:
    ele=int(input())
    if ele==0:
        break
    else:
        a.append(ele)
    sum=0
    for ele in a:
        sum+=ele
print(sum)
# type2
l=[]
n=input('enter numbe br0')
for x in range(len(n)):
    l.append(n[x])
print(l)

#iterate with enumrate instead of range(len())
data=[1,2,3,4,5]
for i in range (len(data)):
    if data [i]<0:
        data[i]=0
print(data)

data=[1,2,3,4,5]
for idx,num in enumerate(data):
    if num<0:
        data[idx]=0
print(data)

# enum and zip


 # ex-1:('with out zip')
nam=['hi','how r u','bharg']
for am in nam:
    print(am)  
#ex-2:(with zip)
nam=['hi','how r u','bharg']
for n in zip(nam):
    print(n)   
                     
 # 2 varibles method
names=['radha','krishna','guru','mahesh']
quals=['queen','king','saviour','devote']
for name,qual in zip(names,quals):
    print(f'{name} is actually {qual}')

# 3 varibles method 
names=['radha','krishna','guru','mahesh']
qual=['queen','king','saviour','devote']
places=['vrindav','vrindava','bulok','bulok']
for name,qual,place in zip(names,qual,places):
    print(f'{name} is actually {qual} from {place}')

# we can iterate list with enumerate 
names=['radha','krishna','guru','mahesh']
qualities=['queen','king','saviour','devote']
for index,name in enumerate(names):
    qual=qualities[index]   # here the change is he saperatedly specify the index with defined varible
    print(f'{name} is actually {qual}')

#if step value is 0 in forward direrection(L to R) and result is always empty
#if step value is -1 in backward direction(R to L) here result is always empty
#ex is print(s[-7:-1:-1])
#when negative indexing default end : -(len(string) + 1)

#negative slicing 
s=[1,2,3,4,5,6,7,8,9]
# print(s[9:1:-1])
# print(s[9:1:-2])
# print(s[8:1:-1]) here it starts after 8 and it stops before 1 that is 2
# print(s[8:1:-2])
print(s[7::-1])
print(s[7::-2])
print(s[-7:1:-1])
print(s[8::-2])

''':
1) l=["A","B","C"] 
2) x=len(l) 
3) for i in range(x): 
4) print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x) 
'''
'''


The process of creating exactly duplicate independent object is called cloning.
We can implement cloning by using slice operator or by using copy() function

x=[10,20,30,40] 
2) y=x[:] 
3) y[1]=777 
4) print(x) ==>[10,20,30,40] 
5) print(y) ==>[10,777,30,40]

2. By using copy() function:
1) x=[10,20,30,40] 
2) y=x.copy() 
3) y[1]=777 
4) print(x) ==>[10,20,30,40] 
5) print(y) ==>[10,777,30,40] 
'''
