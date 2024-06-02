''' lambda is also known as anonymous or no name function or one line function
	its used for instance purpose 
	is possbile to pass one fun to  another function as 
	argument labmda is best choice  
'''

add =lambda a,b:a+b
print(add(12,32,43,46))
 
'''sort a list of tuples
'''
students = [('sai', 18,10.20), ('charan', 30,3.5), ('kumar', 27,4.5), ('cherry', 12,1.2)]

#here key means its asking which index u want to compare among all tuples in list
#if x[0]= str vslues ,x[1]=int,x[2]=float values,

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
 
'''
 
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
#  common elements between 2 list using lambda '''

##
a=[1,2,4,3,5,6]
b=[6,3,8,9,1,2]
common=list(filter(lambda x:x in a,b))
print("common elements from two sets:",common)
 
"""
here what i observed is we can check n no of lists by using 
for x in l1 if x in l2  if x in l3 ....
this is nothing but if loop in vertical direction 
it means that 1st if satisifies again 2nd if and agian 3rd if 

 
  if cond 1:
	  if cond 2:
		  if condi3:
			  and so on...
here i conlcude that  program logics are
 we can mix their formats in different syntaxes

"""