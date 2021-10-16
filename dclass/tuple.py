''' in tuple parenthasis is optional , len(tuple) is also available 
before index method use member ship operator in that so we dont get error(like value in tuple or not )
#*in list we have sort() fun but not in tuple so in tuple we use sorted ()
In sorted (reverse=True ) for values in reverse and descending order
#* tuple comprehension is not in python  
# if  use () this concept is called generator
we can apply + and * operator for tuple
'''
t=()     #tuple
# t=(10,) #tuple
# t=(10)    int
# t=10      int
# t=10,    tuple
# t=10,20  tuple
print(type(t))


# tuple packing and
a=10
b=20
c=30
t=a,b,c
print(t)

# tuple unpacking
t=(10, 20, 30)
a,b,c=t
print(a,b,c)

t=(x*x for x in range (10)) # this is not compreh it is generator obj
for x in t:
    print(x,end='')
#adv of pointers
a,b,*c=(1,2,"hi","bhargav","hgfhfvhmvhmvhjmvhj,vjhvmghc")
print(a)
print(b)
print(c)


#C convert user i/p to tuple ,it cant perform arithmetic operations
tpl =tuple (int(x) for x in input('enter values').split(","))
print(tpl)
print(type(tpl))

#IF __name__='__main__'
if (__name__=='__main__'):
    t1=(1,2,3,4)
    a,b,c,d=t1
    print("Add:-",a+b+c+d)
    print("sub:-",a-b-c-d)
    print("mul:-",a*b*c*d)

#P PACKING AND UNPACKING
t= (2,3,4,5)
a,b,c,d=t

# Write a program that will accept the character as a input
# from user n store it into tuple and convert the tuple into string.

s = input("Enter a string:")
t = tuple(s)  #it taking all values as str not int
# s = tuple(x for x in input().split(","))  # othe way of input
print(type(t))
s1=''.join(t)  # it works in tuple because inside tuple elements are str not int so join works
print("tuple:",t,"\n""string:",s1)

# Write a program that will find the
# repeated elements of the tuple and print 
# how much time they are appearing in tuple.

t=1,2,3,3,2,2,1
s=set(t)
for k in s:
    count=0
    for j in t:
        if k==j:
            count+=1
    print(k,'repeated',count,'times')


t=tuple(input('enter ur tuple'))
s=set(t)
d={}
for k in s:
    d[k]=t.count(k)
for x,y in d.items():
    print('{} times {}'.format(x,y))

#SC way but some mistakes
t1=tuple(input("enter tuple:"))
print("count:",t1.count(int(input("Enter no:"))))

l1 = (1,5,6,2,1,1,2,5,4,87,87,5,4)
s1 = set(l1)
for i in s1:
    print(f'Occurance of {i} is ',l1.count(i),"times")

t=tuple([1,1,2,13,13,14,23,1])
for i in t:
    print(" Count of {} ={}".format(i,t.count(i)))

#item position
tpl = (1 , 3 ,5 ,2 , 4 ,7 ,8 ,6,9)
x = int(input("Enter the element u want to find: "))
for i in range(len(tpl)):
  if tpl[i] == x:
    print(x," is found at position ",i)
    break
else:
    print(x,"is not in the tuple")



# Write a program to replace last values of tuple in a list.

# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

l=[(10,20,40),(20,40,50),(70,80,90)]
print([t[:-1]+(100,)for t in l]) 

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
ans =[]
for i in lst:
  x = list(i)
  x[len(x)-1]=100
  ans.append(tuple(x))
print(ans)



