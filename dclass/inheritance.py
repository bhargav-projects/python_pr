'''
'''

#combining another class 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def name(self):
        print('the person name is ',self.name)
    def age(self):
        print('the person age is ',self.age)
class emp(person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salry=salary
    def empinfo(self):
        print('the emp name is ',self.name)
        print('the emp age is ',self.age)
        print('the emp salry is',self.salry)

p=emp('naresh it',100,10000)
p.empinfo()

#atul bro ans 
class A:
    def __init__(self,a,b):
        super(A,self).__init__(b)
        self.a=a
class B:
    def __init__(self,b):
        self.b=b
class C(A,B):
    def __init__(self, a, b,c):
        super(C,self).__init__(a, b)
        self.c=c
obj=C(1,2,3)
print(obj.a)
print(obj.b)
print(obj.c)



#aishwrya pendkar
class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    
    def get_age(self):
        print(f"Age:{self.age}")
    
    def get_name(self):
        print(f"Name:{self.name}")
        
class employee(person):  
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    
    def display(self):
        print(f"id:{self.id} \nsalary:{self.salary}")
        
s=employee("abc",30,45,50000)  
s.get_name()
s.get_age()
s.display()
              

'''
From P2012--Atul Anand to Everyone:  09:10 AM
class Student:
        stu=list();
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
                               flag=True;
                               print("Name=",i["Name"])
                               print("Gender=",i["Gender"])
                               print("roll=",i["roll"])
                               break;
                if not flag:
                        print("not Found")
                
        def remove():
                key=input("Enter name:-")
                flag=False
                for i in Student.stu:
                       if i["Name"]==key:
                               flag =True
                               Student.stu.remove(i)
break;
                if not flag:
                        print("not Found")
                      

if __name__=='__main__':
        Student.add()
        Student.add()
        Student.show()
        Student.remove()
        Student.show()
From P2026 - Damini Nishane to Everyone:  09:13 AM
class Student:
    student_rn='101'
    student_name='sita'
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_class = 'VII'
Student.student_gender = 'Female'
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\n removing some keys from the studebt class:")
del Student.student_gender 
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')
From P2037 Komal Datta to Everyone:  09:15 AM
question??
From P2004.Aishwarya Pendkar to Everyone:  09:17 AM
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
elif(
elif(ch == 3):
    s.remove()
    print(ls.__len__())
    print("List after deletion")
    for i in range(ls.__len__()):    
        s.display(ls[i])
else:
      print("Invalid choice")
             
    O/P:
1.Add Student details
2.Display Student Details
3.Delete Details of Student
Enter choice:1
Enter name:ABC
Enter Roll no:1
Enter name:XYZ
Enter Roll no:2
Enter name:ASD
Enter Roll no:3
Enter name:ADK
Enter Roll no:4

List of Students

Name   :  ABC
RollNo :  1
Name   :  XYZ
RollNo :  2
Name   :  ASD
RollNo :  3
Name   :  ADK
RollNo :  4
From Anumalla Sai Charan(P2010) to Everyone:  09:18 AM
class Student:
    student_rn='1'
    student_name='sai'
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_class = 'VII'
Student.student_gender = 'male'
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\n removing some keys from the studebt class:")
del Student.student_gender 
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')
From P-2013 atul runwal to Everyone:  09:20 AM
#Write a student class and add methods like add student, show student, remove student studnet rollno student name studnet class using dictionary

class student:
  student_dict={}
  key=0
  def add_student(self):
    self.n=int(input('how many entries'))
    for i in range(0,self.n):
      self.l1=[]
      self.student_name=input('enter student name ')
      self.student_rollno=int(input('enter student rollno '))
      self.student_class=input('enter studnet class')

      self.l1.append(self.student_name)
      self.l1.append(self.student_rollno)
      self.l1.append(self.student_class)
    
      self.key=self.key+1
      self.student_dict[self.key]=self.l1
  def show_student(self):
    self.i=int(input('enter key to display'))
    print(self.student_dict)
    self.values1=self.student_dict[self.i]
    print(self.values1)

  def remove_student(self):
    self.removekey=int(input('enter key to remove'))
    if self.removekey in self.student_dict:
      del self.student_dict[self.removekey]
      print(f'{self
def remove_student(self):
    self.removekey=int(input('enter key to remove'))
    if self.removekey in self.student_dict:
      del self.student_dict[self.removekey]
      print(f'{self.removekey} is removed')
    else:
      print('invalid key')
    print(self.student_dict)
def main():
  s1=student()
  s1.add_student()
  s1.show_student()
  s1.remove_student()
main()                                                                                                                                     output:-how many entries2
enter student name ramesh
enter student rollno 101
enter studnet classp1
enter student name suresh
enter student rollno 102
enter studnet classp2
enter key to display1
{1: ['ramesh', 101, 'p1'], 2: ['suresh', 102, 'p2']}
['ramesh', 101, 'p1']
enter key to remove2
2 is removed
{1: ['ramesh', 101, 'p1']}
From Mahi Avidi to Everyone:  09:21 AM
class Student:
    student_rn='101'
    student_name='sita'
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_class = 'VII'
Student.student_gender = 'Female'
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\n removing some keys from the studebt class:")
del Student.student_gender 
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')
From P2023 Siva suprathi to Everyone:  09:22 AM
dict={}
class Student:
    print("Original attributes and their values of the Student class:",dict)
    def addstudent(self):
       stno=int(input("Enter student number:"))
       dict['number']=stno
       sname = input("Enter student name:")
       dict['name']=sname
       scourse = input("Enter student course:")
       dict['course']=scourse
       dict[id]=dict
       print(dict)
    def removestudent(self):
        if id in dict.keys():
            remove dict[id]


so=Student()
so.addstudent()
so.removestuent()
From P2038 Krishna Rajesh Kotha to Everyone:  09:22 AM
#Write a student class and add methods like add student, show student, remove student
class Student:
    student_rollno='201'
    student_name='rajesh'
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_class = "X"
Student.student_area = "bapatla"
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\n removing keys from student class:")
del Student.student_area 
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

#output
#student_rollno -> 201
#student_name -> rajesh
#student_class -> X
From P-2013 atul runwal to Everyone:  09:22 AM
had sir given any new program ?
From P2004.Aishwarya Pendkar to Everyone:  09:22 AM
no
From P2038 Krishna Rajesh Kotha to Everyone:  09:22 AM
no
From Rushikesh Pawar to Everyone:  09:23 AM
I did not give any new question since only few of you answered the question
I want answer from everyone
From G B N.Sowmya-P2015 to Everyone:  09:27 AM
class Student:
	def __init__(self, name, rollno,age,m1):
		self.name = name
		self.rollno = rollno
		self.age = age
		self.m1 = m1
		
	def accept(self, Name, Rollno,age,marks1 ):
		ob = Student(Name, Rollno,age,marks1,)
		ls.append(ob)

	def display(self, ob):
			print("Name : ", ob.name)
			print("RollNo : ", ob.rollno)
			print("age : ", ob.age)
			print("Marks1 : ", ob.m1)
			print("\n")	
			
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].rollno == rn):
				return i	
								
	def delete(self, rn):
		i = obj.search(rn)
		del ls[i]

ls =[]
obj = Student('', 0, 0, 0)

obj.accept("sowmya", 1,21, 100)
obj.accept("meghana", 2,23, 90)
obj.accept("vasanthi", 3,22, 80)
		
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):	
	obj.display(ls[i])
			
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
		

obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):	
	obj.display(ls[i])
From P2037 Komal Datta to Everyone:  09:31 AM
#Write a student class and add methods like add student, show student, remove student
class Student:
    student_rollno=46
    student_name="Krishna"
   
print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_class = "Btech
Student.student_area = "bapatla"
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\n removing keys from student class:")
del Student.student_area 
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

#output
#student_rollno -> 46
#student_name -> Krishna
#student_class -> Btech
From Preeti Bharti-P2073 to Everyone:  09:31 AM
class Student:
    student_roll='1'
    student_name='sk'
   
print(" Show the student details:")
for k, v in Student.__dict__.items():
    if not k.startswith('_'):
        print(f'{key} : {value}')

print(" Details added into student class:")
Student.student_class = 'x'
Student.student_gender = 'male'
for k, v in Student.__dict__.items():
    if not k.startswith('_'):
        print(f'{key} : {value}')

print("Removing some keys from the studebt class:")
del Student.student_gender 
for k, v in Student.__dict__.items():
    if not k.startswith('_'):
        print(f'{key} : {value}')
From P2024 BOGA BINDUPRIYA to Everyone:  09:33 AM
class student():
	def __init__(self,name,rollno):
		self.Name=name
		self.RollNo=rollno
	def add(self,Name,RollNo):
		for i in range(3):
			Name=input("Student name:")
			RollNo=int(input("Roll number:"))
			d=student(Name,RollNo)
			ls.append(d)
	def show(self,d):
		print("Student Name:",d.Name)
		print("Student roll number:",d.RollNo)
		
	def remove(self):
		del(self.Name)
		del(self.RollNo)
		print("deleted student details")
ls=[]
s=student(",0)
print("1.Add,2.show,3.Delete")
ch=int(input("enter"))
if(ch==1):
	s.add(",0)
	print("students list")
	for i in range(ls.__len__()):
		s.show(ls[i])
elif(ch==2):
	print("students list")
	for i in range(ls.__len__()):
		s.show(ls[i])
elif(ch==3):
	s.remove()
	print(ls.__len__())
	print("list")
	for i in range(ls.__len__()):
		s.show()
From P2023 Siva suprathi to Everyone:  09:38 AM
class Student:
    def __init__(self, name, rollno,course):
        self.name = name
        self.rollno = rollno
        self.course=course
    def accept(self, Name, Rollno, marks1,course):
        ob = Student(Name, Rollno, marks1,course)
        dict.add(ob)
    def display(self, ob):
        print("Name   : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("course : ", ob.course)
    def delete(self, rn):
        i = obj.search(rn)
        del dict[i]


dict = dict()

obj = Student('', 0, 0, 0)
obj.accept("A", 1, "python")
obj.accept("B", 2,"Java")
obj.accept("C", 3,"c++")
print("List of Students")
for i in range(dict.__len__()):
    obj.display(dict[i])

print(" Student Found, ")
s = obj.search(2)
obj.display(dict[s])

obj.delete(2)
print(dict.__len__())
print("List after deletion")
for i in range(dict.__len__()):
    obj.display(dict[i])
From P2030-G.Udaya Bhanu to Everyone:  09:40 AM
class Student:
  
     name = ' '
  
     clg = ' '
  
     rno = 0
   
    def add(self,name, clg, rno):
    
        self.name=name
  
        self.clg = clg
  
        self.rno = rno
 
   def show(self):
  
         print("Student details")
 
         print('Name: ', self.name)
     
         print('College: ',self.clg)
  
         print('Rool no: ',self.rno)

s = Student()

s.add('Nani','svr',17504)

s.show()

OUTPUT:
Student details
Name: Nani
College:svr
Roolno:17504
From Rushikesh Pawar to Everyone:  09:40 AM
Write a program to create a person class which have two methods i.e name and age and create another class i.e employee which inherit all the methods of person class and also have his own methods like empid and salary.
From P-2013 atul runwal to Everyone:  09:44 AM
sir once again please
all should be accessed from employee class?
From Me to Rushikesh Pawar:  (Direct Message) 09:48 AM
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def name(self):
        print('the person name is ',self.name)
    def age(self):
        print('the person age is ',self.age)
class emp(person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salry=salary
    def empinfo(self):
        print('the emp name is ',self.name)
        print('the emp age is ',self.age)
        print('the emp salry is',self.salry)

p=emp('naresh it',100,10000)
p.empinfo()

# #the emp name is  naresh it
# the emp age is  100
# the emp salry is 10000
sir is it correct?
From Me to Everyone:  09:48 AM
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def name(self):
        print('the person name is ',self.name)
    def age(self):
        print('the person age is ',self.age)
class emp(person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salry=salary
    def empinfo(self):
        print('the emp name is ',self.name)
        print('the emp age is ',self.age)
        print('the emp salry is',self.salry)

p=emp('naresh it',100,10000)
p.empinfo()

# #the emp name is  naresh it
# the emp age is  100
# the emp salry is 10000
From P2012--Atul Anand to Everyone:  09:50 AM
class Name:
        def __init__(self,name,age):
                self.name=name;
                self.age=age;
        def getName(self):
                return self.name;
        def getAge(self):
                return self.age;
class Emp(Name):
        def __init__(self,name,age,empid,salary):
                super().__init__(name,age);
                self.empid=empid;
                self.salary=salary;
        def getEmpid(self):
                return self.empid
        def getEmpsal(self):
                return self.salary
                      

if __name__=='__main__':
        e=Emp('atul',22,"Em101",40000)
        print("ID:-",e.getEmpid())
        print("NAME:-",e.getName())
        print("AGE:-",e.getAge())
        print("SALARY:-",e.getEmpsal())
#output:- 
ID:- Em101
NAME:- atul
AGE:- 22
SALARY:- 40000
From P2004.Aishwarya Pendkar to Everyone:  09:54 AM
class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    
    def get_age(self):
        print(f"Age:{self.age}")
    
    def get_name(self):
        print(f"Name:{self.name}")
        
class employee(person):  
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    
    def display(self):
        print(f"id:{self.id} \nsalary:{self.salary}")
        
s=employee("abc",30,45,50000)  
s.get_name()
s.get_age()
s.display()
              
Name:abc
Age:30
id:45 
salary:50000
From Anumalla Sai Charan(P2010) to Everyone:  09:59 AM
class Person(object):
    def __init__(self, name, age):
	    self.name = name
	    self.age = age
    def getName(self):
	    return self.name
    def getAge(self):
            return self.age

    def isEmployee(self):
	    return False
class Employee(Person):
	def isEmployee(self):
		return True
emp = Person("sai1",20)
print(emp.getName(), emp.getAge(), emp.isEmployee())

emp = Employee("sai2",30)
print(emp.getName(),emp.getAge(), emp.isEmployee())
output
sai1 20 False
sai2 30 True
>>>
From Rushikesh Pawar to Me:  (Direct Message) 09:59 AM
yes its correct
From P2023 Siva suprathi to Everyone:  09:59 AM
class Person:
    def getpersondet(self):
        self.pname="xxx"
        self.page="30"
    def disppersondet(self):
        print("person name:", self.pname)
        print("person age:", self.page)

class Employee(Person):
    def getempdet(self):
        self.empno=121
        self.empname="yyy"
        self.empsal=40000
        self.getpersondet()
    def dispempdet(self):
        print("Employee number:",self.empno)
        print("Employee name:", self.empname)
        print("Employee salary:", self.empsal)
        self.disppersondet()

eo=Employee()
eo.getempdet()
eo.dispempdet()                                             output:-Employee number: 121
Employee name: yyy
Employee salary: 40000
person name: xxx
person age: 30
From Me to Rushikesh Pawar:  (Direct Message) 10:00 AM
thank you sir
From Anumalla Sai Charan(P2010) to Everyone:  10:00 AM
ok sir
From P2026 - Damini Nishane to Everyone:  10:00 AM
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def getname(self):
        print("Name:",self.name) 
    def getage(self):
        print("Age:",self.age)
class Employee(person):
    def __init__(self, name, age, empid, empsalary):
        super().__init__(name, age)
        self.empid = empid
        self.empsalary = empsalary
    def displaydata(self):   
        print("id:", self.empid)
        print("Salary:", self.empsalary)

emp = Employee('Tessa', 35, 1001, 30000)
emp.getname()
emp.getage()
emp.displaydata()
From P2007-Alwala Sharanya to Everyone:  10:01 AM
class details:
	def getnam(self):
		self.nam="rossum"
class age:
	def getagedet(self):
		self.age=60
class employee(details,age):
	def getempdet(self):
		self.empid=123
		self.ename="gs"
		self.sal=1500
	def dispempdet(self):
		print("employeeid:{}".format(self.empid))
		print("employe name:{}".format(self.ename))
		print("employe sal:{}".format(self.sal))
		print("name:{}".format(self.nam))
		print("age:{}".format(self.age))
eo=employee()
eo.getnam()
eo.getagedet()
eo.getempdet()
eo.dispempdet()


E:\praticcceeee>py new.py
employeeid:123
employe name:gs
employe sal:1500
name:rossum
age:60
From Anumalla Sai Charan(P2010) to Everyone:  10:01 AM
id and salary in child class sir
ok sir
From P2023 Siva suprathi to Everyone:  10:01 AM
class Person:
    def getpersondet(self):
        self.pname="xxx"
        self.page="30"
    def disppersondet(self):
        print("person name:", self.pname)
        print("person age:", self.page)

class Employee(Person):
    def getempdet(self):
        self.empno=121
        self.empname="yyy"
        self.empsal=40000
        self.getpersondet()
    def dispempdet(self):
        print("Employee number:",self.empno)
        print("Employee name:", self.empname)
        print("Employee salary:", self.empsal)
        self.disppersondet()

eo=Employee()
eo.getempdet()
eo.dispempdet()
From P2017- BASAVA CHETAN to Everyone:  10:05 AM
class person:                                                    def__init__(self, name, age)                            self.name=name                                               self.age=age                                                 def name(self) :                                                 print("the name of person is:", self.name)                 def age(self) :                                                       print("the age is:", self.age)                                          class employee                          def__init__(self, name, age, salary)                 super().__init__(name,age)                                      self.salary=salary                                                           def emp(self)                                                    print("the employee name is:", self.name)             print("the age is:", self.age)                                 if__name__='__main__':                                                 x=emp('naresh', 25, 25000)
From P2002 Adesh Jolhe to Everyone:  10:05 AM
class Person:
        def __init__(self, pnm, page):
            self.name = pnm
            self.age = page

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age


class Employee(Person):
    def __init__(self, name, age, empid, salary):
        super().__init__(name, age)
        self.empid = empid
        self.salary = salary

    def get_empid(self):
        return self.empid

    def get_empsal(self):
        return self.salary


if __name__ == '__main__':
    emp1 = Employee(name = "Adesh", age = 23, empid = 101, salary = 156485.25)
    print("Id : ", emp1.get_empid())
    print("Name : ", emp1.get_name())
    print("Age : ", emp1.get_age())
    print("Salary : ", emp1.get_empsal())
# Output :
# Id :  101
# Name :  Adesh
# Age :  23
# Salary :  156485.25
From Preeti Bharti-P2073 to Everyone:  10:06 AM
class Person:
    def getpersondet(self):
        self.pname=input ("enter person name:")
        self.page=int(input ("enter person age:"))
class Employee(Person):
    def getempdet(self):
        self.empname=input("enter employee name:")
        self.empage=int(input("enter employee age:")
        self.empid=int(input ("enter employee id:"))
        self.empsal=input ("enter employee salary:")
    def dispempdet(self):
        print("employee details:")
        print ("employee name:{}",.format(self.empname))
        print ("employee age:{}",.format(self.empage))
       print ("employee id:{}",.format(self.empid))
      print ("employee salary:{}",.format(self.empsal))
eo=Employee()
eo.getpersondet()
eo.getempdet()
eo.dispempdet()
From P2024 BOGA BINDUPRIYA to Everyone:  10:06 AM
class employee:
	def getempdet(self,name,age):
		self.name="ABC"
		self.age=25
class details(employee):
	def getdet(self):
		self.empid=120
		self.salary="4L"
	def dispempdet(self):
		print("employee number:",self.empid)
		print("employee name:",self.name)
		print("employee age:",self.age)
		print("employee salary:",self.salary)

e=details()
e.getempdet()
e.getdet()
e.dispempdet
From P2017- BASAVA CHETAN to Everyone:  10:07 AM
print("name:", x.getname())                                  print("age:", x.getage())                                     print ("salary:", x.getsalary())
class person:                                                    def__init__(self, name, age)                            self.name=name                                               self.age=age                                                 def name(self) :                                                 print("the name of person is:", self.name)                 def age(self) :                                                       print("the age is:", self.age)                                          class employee                          def__init__(self, name, age, salary)                 super().__init__(name,age)                                      self.salary=salary                                                           def emp(self)                                                    print("the employee name is:", self.name)             print("the age is:", self.age)                                 if__name__='__main__':                                                 x=emp('naresh', 25, 25000)
From P2017- BASAVA CHETAN to Everyone:  10:07 AM
print("name:", x.getname())                                  print("age:", x.getage())                                     print ("salary:", x.getsalary())
From Mahi Avidi to Everyone:  10:08 AM
class Person:
    def getpersondet(self):
        self.pname="Raju"
        self.page="25"
    def disppersondet(self):
        print("person name:", self.pname)
        print("person age:", self.page)

class Employee(Person):
    def getempdet(self):
        self.empno=2014
        self.empname="Ramya"
        self.empsal=50000
        self.getpersondet()
    def dispempdet(self):
        print("Employee number:",self.empno)
        print("Employee name:", self.empname)
        print("Employee salary:", self.empsal)
        self.disppersondet()

eo=Employee()
eo.getempdet()
eo.dispempdet()                                             output:-Employee number: 121
Employee name: Ramya
Employee salary: 50000
person name: Raju
person age: 25
From P2038 Krishna Rajesh Kotha to Everyone:  10:09 AM
#Write a program to create a person class which have two methods i.e name and age and create another class i.e employee which inherit all the methods of person class and also have his own methods like empid and salary.
class Person:
	def __init__(self, name, age):
		self.name=name
		self.age=age
		def getName(self):
			return self.name
		def getage(self):
			return self.age

class employee(Person):
   def __init__(self, name, age, empid, salary):
	   super().__init__(name, age)
	   self.empid = empid
	   self.salary = salary
	   def employeeinfo(self):
		   print('the emp name is ',self.name)
		   print('the emp age is ',self.age)
		   print('the emp empid is',self.empid)
		   print('the emp salry is',self.salry)

p=employee('kkr',26,"P2038",10000)
p.employeeinfo()
#output
#the emp name is kkr
#the emp age is 26
#the emp empid is P2038
#the emp salary is 10000
From P2064-nishat fatima to Everyone:  10:13 AM
class Person:
    def getpersondet(self):
        self.pname="xxx"
        self.page="30"
    def disppersondet(self):
        print("person name:", self.pname)
        print("person age:", self.page)

class Employee(Person):
    def getempdet(self):
        self.empno=121
        self.empname="yyy"
        self.empsal=40000
        self.getpersondet()
    def dispempdet(self):
        print("Employee number:",self.empno)
        print("Employee name:", self.empname)
        print("Employee s salary:", self.empsal)
        self.disppersondet()

eo=Employee()
eo.getempdet()
eo.dispempdet()
From G B N.Sowmya-P2015 to Everyone:  10:13 AM
class Person( object ):	
		
		def __init__(self, name, idnumber,salary):
				self.name = name
				self.idnumber = idnumber
				self.salary = salary
		def display(self):
				print(self.name)
				print(self.idnumber)
				print(self.salary)

class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				Person.__init__(self, name, idnumber,salary)
				
				
a= Employee('sowmya', 886012, 200000, "Intern")

a.display()
From P2064-nishat fatima to Everyone:  10:17 AM
class Person:
    def getpersondet(self):
        self.pname="xxx"
        self.page="30"
    def disppersondet(self):
        print("person name:", self.pname)
        print("person age:", self.page)

class Employee(Person):
    def getempdet(self):
        self.empno=121
        self.empname="yyy"
        self.empsal=40000
        self.getpersondet()
    def dispempdet(self):
        print("Employee number:",self.empno)
        print("Employee name:", self.empname)
        print("Employee s salary:", self.empsal)
        self.disppersondet()

eo=Employee()
eo.getempdet()
eo.dispempdet()
class person():
    def description(self):
        self.name ='xyz'
        self.age = 60
    def man(self):
        print("person name:",self.name)
        print("person age:",self.age)
        
class Employee(person):
    def getemp(self):
        self.empyid =2064
        self.empysalary=25000
        self.empyname="pop"
        self.empyage=56
    def dispemp(self):
        print("Employee id:",self.empyid)
        print("Employee salary:", self.empysalary)
        print("Employee name:", self.empyname)
        print("Employee age:", self.empyage)
        self.man()

emp=Employee()
emp.getemp()
emp.dispemp()
From G B N.Sowmya-P2015 to Everyone:  10:21 AM
ok sir
From Anumalla Sai Charan(P2010) to Everyone:  10:22 AM
Name: sai
Age: 20
id: 1
Salary: 2000
>>>
class person:  def __init__(self,name,age):     self.name = name     self.age = age
       def getName(self):      print("Name:",self.name)   def getAge(self):      print("Age:",self.age)class Employee(person):  def __init__(self,name,age,empid,empsalary):     super().__init__(name, age)     self.empid = empid     self.empsalary = empsalary  def displayData(self):        print("id:", self.empid)     print("Salary:", self.empsalary)
emp=Employee("sai",20,1,2000)
emp.getName()
emp.getAge()
emp.displayData()
output
Name: sai
Age: 20
id: 1
Salary: 2000
>>>
From P-2013 atul runwal to Everyone:  10:31 AM
#Write a program to create a person class which have two methods i.e 
#name and age and create another class i.e employee which inherit all the 
#methods of person class and also have his own methods like empid and salary.

class person:
  def _init_(self):
    self.person_age=None
    self.person_name=None
  def get_person_details(self):
    self.person_name=input('enter name')
    self.person_age=int(input('enter age'))
class employee(person):
  def _init_(self):
    self.empid=None
    self.empsal=None
    super()._init_(self)
  def get_employee_details(self):
    super().get_person_details()
    self.empid=int(input('enter id'))
    self.empsal=int(input('enter salary'))
    
  def get_details(self):
    print(f'employee id : {self.empid}\nname:{self.person_name}\nage: {self.person_age}\nsalar: {self.empsal}')
def main():
  e1=employee()
  e1.get_employee_details()
  e1.get_details()
main()
enter namekaran
enter age45
enter id101
enter salary50000
employee id : 101
name:karan
age: 45
salar: 50000
From Rushikesh Pawar to Me:  (Direct Message) 10:38 AM
Write a program to show the example of multiple inheritance.
From Rushikesh Pawar to Everyone:  10:38 AM
Write a program to show the example of multiple inheritance.
From P2004.Aishwarya Pendkar to Everyone:  10:39 AM
yes
From Anumalla Sai Charan(P2010) to Everyone:  10:39 AM
s sir
From P2064-nishat fatima to Everyone:  10:39 AM
yes
From Preeti Bharti-P2073 to Everyone:  10:39 AM
yes sir
From P2026 - Damini Nishane to Everyone:  10:39 AM
yes sir
From P2012--Atul Anand to Everyone:  10:39 AM
yes sir got it
From P2007-Alwala Sharanya to Everyone:  10:41 AM
yes sir
From Me to Everyone:  10:44 AM
class parent:
    def p1():
        print('this is parent class ')
class mother:
    def m1():
        print('this is mother class ')

class grnadmother:
    def gm1():
        print('this is grnadmother class ')

class me(parent,mother,grnadmother):
    def main():
        print('this is my parent details')
        p=parent
        p.p1()
        m=mother
        m.m1()
        gm=grnadmother
        gm.gm1
        print('end')
me.main()

# output:
# this is my parent details
# this is parent class 
# this is mother class
# end
From Anumalla Sai Charan(P2010) to Everyone:  10:45 AM
class Car:
    def name(self):
        print("Car")
 
class Bus(Car):
    def name(self):
        print("bus")
        super().name()
 
class Bike(Car):
    def name(self):
        print("bike")
        super().name()
 
class Vehicle(Bus, Bike):
    def m(self):
        print("vehicle")  
        super().name()
      
obj = Vehicle()
obj.m()
out put:
vehicle
bus
bike
Car
>>>
From P2026 - Damini Nishane to Everyone:  10:48 AM
class A:
    def a(self):
        print("this is 1st class")
class B(A):
    def a(self):
        print("this is 2nd class")
class C(A):
    def a(self):
        print("this is 3rd class")
class D(B,C):
    def a(self):
        print("this is 4th class")

obj = C()
obj.a()
D.a(obj)
B.a(obj)
A.a(obj)
output:this is 3rd class
this is 4th class
this is 2nd class
this is 1st class
From Me to Everyone:  10:49 AM
class parent:
    def p1(self):
        print('this is parent class ')
class mother:
    def m1(self):
        print('this is mother class ')

class grnadmother:
    def gm1(self):
        print('this is grnadmother class ')

class me(parent,mother,grnadmother):
   ...

#calling out side of child class by inheriting from parent classes 
m=me()
m.p1()
m.m1()
m.gm1()

# output:
# this is my parent details
# this is parent class 
# this is mother class
From P2023 Siva suprathi to Everyone:  10:49 AM
class car:
    def getcardet(self):
        self.cname="BMW"
        self.ccolor="Blue"
class Fruit:
        def getfruitdet(self):
            self.fname="mango"
            self.fcolor="yelllow"
class Person(car,Fruit):
    def getpersondet(self):
        self.pname="xxx"
        self.page=40
    def disppersondet(self):
        print("person name:",self.pname)
        print("person age:", self.page)
        print("person car:", self.cname)
        print("person car color:", self.ccolor)
        print("person favourite fruit:", self.fname)
        print("person favourite fruit color:", self.fcolor)
po=Person()
po.getcardet()
po.getfruitdet()
po.getpersondet()
po.disppersondet()                                                             output:-person name: xxx
person age: 40
person car: BMW
person car color: Blue
person favourite fruit: mango
person favourite fruit color: yelllow
From Me to Everyone:  10:50 AM
sai charan bro ur code logic is hierarchy inheritance
From Anumalla Sai Charan(P2010) to Everyone:  10:51 AM
both hierarchy and multiple
From Mahi Avidi to Everyone:  10:51 AM
class first:
    def f1():
        print('this is first class ')
class second:
    def s1():
        print('this is second class ')

class third:
    def t1():
        print('this is third class ')

class me(first,second,third):
    def main():
        print('this is my first details')
        f=first
        f.f1()
        s=second
        s.s1()
        t=third
        t.t1
        print('end')
me.main()

output:
    
this is my first details
this is first class 
this is second class 
end
From Me to Everyone:  10:51 AM
yes bro but sir said only multiple no hierarchy any way gd bro
From P2002 Adesh Jolhe to Everyone:  10:52 AM
class Person:
        def __init__(self, pnm, page):
            self.name = pnm
            self.age = page

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age


class Student():
    def __init__(self, rollno, marks):
        self.rollno = rollno
        self.marks = marks

    def get_empid(self):
        return self.rollno

    def get_empsal(self):
        return self.marks


class Resident(Person, Student): # extends both Person and Student class
    def __init__(self, name, age, rollno,marks):
        Person.__init__(self, name, age)
        Student.__init__(self,rollno,marks)

if __name__ == '__main__':
    res1 = Resident(name = "Adesh", age = 23, rollno = 101, marks = 14566)
    print("Id : ", res1.get_empid())
    print("Name : ", res1.get_name())
    print("Age : ", res1.get_age())
    print("Salary : ", res1.get_empsal())
# Output :
Id :  101
Name :  Adesh
Age :  23
Salary :  14566
From P2017- BASAVA CHETAN to Everyone:  10:52 AM
class apple:
    def name(self):
        print("apple")
 
class mango(apple):
    def name(self):
        print("mango")
        super().name()
 
class orange(apple):
    def name(self):
        print("orange")
        super().name()
 
class fruits(mango, orange):
    def new(self):
        print("newfruits")  
        super().name()
      
obj =fruits()
obj.new()
                                                               out put:
Newfruits
Mango 
Orange 
Apple
From P2038 Krishna Rajesh Kotha to Everyone:  10:53 AM
#Write a program to show the example of multiple inheritance.
class rajesh:
    def r1():
        print('this is rajesh')
class father:
    def f1():
        print("this is rajesh's father")

class mother:
    def m1():
        print("this is rajesh's mother")

class me(rajesh,father,mother):
    def main():
        print('this is me rajesh')
        r=rajesh
        r.r1()
        f=father
        f.f1()
        m=mother
        m.m1()
me.main()
# output
#this is me rajesh
#this is rajesh
#this is rajesh's father
#this is rajesh's mother
From P2012--Atul Anand to Everyone:  10:54 AM
class A:
        def __init__(self,a):
                self.a=a

class B:
        def  __init__(self,b):
                self.b=b;
        
class C(A,B):
        def __init__(self,a,b,c):
                super(C,self).__init__(a);
                super(C,self).__init__(b);
                self.c=c;
                      

if __name__=='__main__':
        obj=C(1,2,3);
        print(obj.a);
        print(obj.b);
        print(obj.c);
From P2007-Alwala Sharanya to Everyone:  10:55 AM
class companydetails:
	def getcompdet(self):
		self.cnam="wipro"
		self.comploc="hyderabad"
class availablejobs:
	def getjobdet(self):
		self.designation="SE"
class student(companydetails,availablejobs):
	def getstudet(self):
		self.sid=123
		self.sname="gs"
		self.scourses="python"
	def dispstudet(self):
		print("sid:{}".format(self.sid))
		print("sname:{}".format(self.sname))
		print("scourses:{}".format(self.scourses))
		print("cnam:{}".format(self.cnam))
		print("comploc:{}".format(self.comploc))
		print("designation:{}".format(self.designation))
so=student()
so.getcompdet()
so.getjobdet()
so.getstudet()
so.dispstudet()
E:\praticcceeee>py inher.py
sid:123
sname:gs
scourses:python
cnam:wipro
comploc:hyderabad
designation:SE
From P2004.Aishwarya Pendkar to Everyone:  10:56 AM
class person:
    def __init__(self,age,name):
        self.age=45
        self.name="abc"    

class employee:
    def __init__(self):
        self.id=45
        
class salary(person,employee):  
    def __init__(self,name,age,id,salary):
        self.salary=40000
        person.__init__(self, age,name) 
        employee.__init__(self)
        print(f"Name:{self.name}\nAge:{self.age}\nid:{self.id}\nSalary:{self.salary}")      
   
        
s=salary("abc",45,54,40000) 
o/p 
Name:abc
Age:45
id:45
Salary:40000
From P2024 BOGA BINDUPRIYA to Everyone:  10:57 AM
class A:
	def one():
		print("This is class A")
class B:
	def two():
		print("This is class B")
class C:
	def three():
		print("This is class C")
class multiple(A,B,C):
	def main():
		A.one()
		B.two()
		C.three()
multiple.main()
From P2012--Atul Anand to Everyone:  11:00 AM
class A:
        def __init__(self,a):
                self.a=a

class B:
        def  __init__(self,b):
                self.b=b;
        
class C:
        def __init__(self,a,b,c):
                A.__init__(self,a);
                B.__init__(self,b);
                self.c=c;
                      

if __name__=='__main__':
        obj=C(1,2,3);
        print(obj.a);
        print(obj.b);
        print(obj.c);
useing super we can go to parents init
'''