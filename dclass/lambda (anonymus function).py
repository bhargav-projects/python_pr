''' lambda is also known as anonymous or no name fun
its used for instance purpose 
is possbile to pass one fun to  another function as  argument labmda is best choice  
'''

add =lambda a,b,c,d:a+b+c+d
print(add(12,32,43,46))

#
s=lambda n:n*n
print(s(2))
print(s(4))


#
s=lambda a,b,c:a if a>b and a>c  else b if b>c else c
print(s(2,3,6))

#
s=lambda a,b:a if a>b else b 
print(s(2,3))
print('the biggest of {}and {} is {}'.format(10,20,s(10,20)))

''' 
lambda function that adds the multiplies  
'''

#aa
n1,n2=int(input("Enter Number:- ")),int(input("Enter Number:-"))
fun,fun1=lambda n1,n2:n1+n2,lambda n1,n2:n1*n2
print('add',fun(n1,n2),'\n','mul',fun1(n1,n2))

#ap
b=5
x = lambda a: a+5  #s = lambda a : a+5
print("sum:",s(int(input("Enter no"))))
print(x(b)) # we are printing directly calling lambda expression
m = lambda x, y : x * y
print("multi:",m(5,5))

'''sort a list of tuples
'''

students = [('sai', 18,10.20), ('charan', 30,3.5), ('kumar', 27,4.5), ('cherry', 12,1.2)]
print("Original tuples:")
print(students)

#here key means its asking which index u want to compare among all tuples in list
#if x[0]= it comapares names,x[1]=int,x[2]=float values,
#if i try to do x[3] we get index out of range

students.sort(key = lambda x: x[0])
print("\nSorted Tuples:")
print(students)
students.sort(key = lambda x: x[1])
print(students)
students.sort(key = lambda x: x[2])
print(students)
#tuple index out of range because there is no 3rd index
print(students.sort(key = lambda x: x[3]))

#type 2 using sorted
student_data = [("Aman",23),("Adesh",22),("Ankush",24),("Somesh",25)]
print("Before sorting  : ",student_data)
print("After sorting : ",sorted(student_data, key = lambda x: x[1]))

#without lambda
students = [('sai', 18), ('charan', 30), ('kumar', 27), ('cherry', 12),('bhaa',1)]
#its cant print direct print(students.sort())
students.sort() 
print(students)

'''
sort the odd and even number 
from given number of list using lambda function.

'''

l=[1,7,2,9,3,6,4,8,5]
even,odd=list(filter(lambda x:x%2==0 ,l)),list(filter(lambda x:x%2 !=0 ,l))
print('original list',l)
print('even ',sorted(even),'odd',sorted(odd))

'''
whether a given string starts
with a given character using Lambda function.

'''
#aa
s='abc'
c='a'
s1='abc'
c1='z'

fun=lambda a,b: a[0]==b  
#a[0]=='b' if u watn to check particular letter
print(fun(s,c))
print(fun(s1,c1))

# isstartswith
x = lambda x:True if x.startswith('p') else False
print(x('python'))

# user input
b=input('eneter char u want to start')
start = lambda x: True if x.startswith(b) else False
s=input("enter a string")
print(start(s))

# user input type 2
s=input("enter a string=")
c=lambda s:"yes" if (s[0]=="w") else "no"
print(c(s))

#
x,y='bhargav','b'
l=(True if x[0]==y else False )
print(l)

x,y='bhargav','b'
l=(True if y.startswith(x[0])else False )
print(l)

#Write a  program to extract 
# year, month, date and time using Lambda function

#aa
import datetime as dt
d=input("Enter date")
d1=dt.datetime.strptime(d,"%d-%m-%Y")
fun=lambda d1:(d1.day,d1.month,d1.year)
d,m,y=fun(d1)
print(d,m,y,sep="\n")

##
date,month,year=map(int,input('enterdate').split())
print(date,month,year)
datelambda=lambda x:date
monthlambda=lambda y:month
yearlambda=lambda z:year
print(datelambda(date))
print(monthlambda(month))
print(yearlambda(year))    

####
import datetime
# instead of int we can use eval()
yy,mm,dd=map(int,input('Enter date in yyyy/mm/dd format : ').split("/"))
date = datetime.date(yy,mm,dd)
hour,minute,sec = map(int,input("Enter a time in hh:mm:ss format : ").split(":"))
t = datetime.time(hour,minute,sec)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
print("Year : ",year(date))
print("Month : ",month(date))
print("Day : ",day(date))
print("Time : ",t)

'''
 common elements between 2 list using lambda '''

##
a=[1,2,4,3,5,6]
b=[6,3,8,9,1,2]
print("original lists:",a,b)
common=list(filter(lambda x:x in a,b))
print("common elements from two sets:",common)

##aa
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]

fun=lambda list1,list2 : [x for x in list1 if x in list2]

print(fun(l1,l2))  

#here what i observed is we can check n no of lists by using 
# for x in l1 if x in l2  if x in l3 ....this is nothing but if loop in vertical direction 
#it means that 1st if satisifies again 2nd if and agian 3rd if 
'''
  if cond 1:
	  if cond 2:
		  if condi3:
			  and so on...
here i conlcude that  program logics are we can mix their formats in different syntaxes
'''