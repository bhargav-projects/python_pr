'''


'''
#Write a program to create
#a function that will work like range function.
def myRange(start,stop,step=1):
        while(start<stop):
                yield start
                start+=step

if __name__=='__main__':
        for i in myRange(0,5,1):
                print(i)

#
def number(a,b,c):
    while(a < b):
        i =a
        print(i)
        a = a+c
a = int(input('Enter min vlue: '))
b= int(input('Enter max range: '))
c = int(input('Enter step value: '))
number(a,b,c)

#start and end
def fun1(a,b):
  a=a
  b=b
  while a!=b:
    print(a)
    a+=1
def main():
  a=int ( input ('enter start value'))
  b= int ( input ('enter end value'))
  fun1(a,b)
main()     

#
def myrange(start, stop=0, step=1):
	if(start>0 and stop==0):
		i=0	
		while(i< start):
			print(i, end=" ")
			i += step
	elif(start==0 and stop >0):
		while(start<stop):
			print(start, end=" ")
			start += step
	else:
		while(start < stop):
			print(start, end=" ")
			start += step
		
myrange(0 ,10,2)

#dictionary key to get emp det
def emp(key):
        d={1:['atul',40000,'eng'],2:['sagar',20000,'xyz'],3:['Nehal',30000,'y'],4:['Arjun',40000,'a']}
        return d[key]
if __name__=='__main__':
        key=int(input("Enter key:-"))
        l=emp(key)
        print("Name:",l[0])
        print("salary:",l[1])
        print("job role:",l[2])

#
def myRange(*s):
        le=len(s)
        if le==1:
                start,stop,step=0,s[0],1;
        elif le==2:
                start,stop,step=s[0],s[1],1;
        elif le==3:
                 start,stop,step=s;
        else:
                print("Not accepted argument more then three and less then one")
                return
        if step==0:
                print("step must not be zero")
                return
        elif step<0:
                while(start>stop):
                        yield start;
                        start+=step;
        else:
                while(start<stop):
                        yield start;
                        start+=step;
if __name__=='__main__':
        for i in myRange():
                print(i)

#student data
import sys
class Student:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def add_student(self):
        print('student name is',self.name)
        print('student roll no is',self.number)
        
    def removeStudent(self):
        print('deleting student name and number',self.name,self.number)
        del(self.name)
        del(self.number)
        print('deleted student successfully')



while True:
    print('add student \n remove student' )
    option=input('choose ur option')
    if option=='add' :
       name=input('enter s name')
       number=int(input('enter number'))
       s=Student(name,number)
       s.add_student()
    elif option=='remove':
        name=input('enter s name')
        number=int(input('enter number'))
        s.removeStudent()
    elif option=='e' or 'E':
        sys.exit()
    else:
        print('invalid ooption thank u')


#storing studnet data
class Student:
        stu=[]
        def add():
                d={"Name":input("Enter Name:-"),
                   "Gender":input("Enter gender:-"),
                   "roll":int(input("Enter roll:-"))}
                Student.stu.append(d);
        def show():
                key=input("Enter name:-")
                flag=False
                for i in Student.stu:
                       if i["Name"]==key:
                               flag=True
                               print("Name=",i["Name"])
                               print("Gender=",i["Gender"])
                               print("roll=",i["roll"])
                               break
                if not flag:
                        print("not Found")
                
        def remove():
                key=input("Enter name:-")
                flag=False
                for i in Student.stu:
                       if i["Name"]==key:
                               flag =True
                               Student.stu.remove(i)
s=Student
s.add()
s.show()


#
class Car:
	brand = "BMW"
	color = "Black"
if __name__ =='__main__':
	c1 = Car()
	print("Brand: ",c1.brand)
	print("Color: ",c1.color)
Brand: BMW
Color: Black

#
class fruit:
    def __init__(self,color,name):
        self.Color=color
        self.Name = name
    def display(self):
        print(f"color={self.Color},Name = {self.Name}")
    
f = fruit("Red","Apple")
f.display()
f.Name="BANANA"
f.Color='yellow'
f.display()

#
class Fruit:
	type="Apple"
	color="Red"
	nos=5

	def __init__(self,type,color,nos):
		self.type=type
		self.color=color
		self.nos=nos

	def display(self):
		print("Name of the fruit is :",Fruit.type)
		print("Color of the fruit is :",Fruit.color)
		print("Number of the fruits is :",Fruit.nos)

		print("Name of the fruit is :",self.type)
		print("Color of the fruit is :",self.color)
		print("Number of the fruits is :",self.nos)

f=Fruit("kiwi","green",3)
f.display()

#changing previous varibles details
class Fruit:
	name ="Banana"
	taste = "Sweet"
f = Fruit()
f.name = "Mango"
f.taste = "Sour"
print(f.name)
print(f.taste)



   




        




