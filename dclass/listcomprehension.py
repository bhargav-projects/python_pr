'''


'''
#C cubes
l1=[x**3 for x in range(12,17)]
print(l1)

# by using math Module
from math import pow
x = [int(pow(i,3)) for i in range(0,5)]
print("cube=",x)    

# by taking creating obj
lst = [1,2,5,9,7,6,32]  # this creating list obj
cube_list = [i**3 for i in lst]
print('cube of numbers is :',cube_list)

l,cube=[1,2],[]
for ele in l:
    cube.append(ele**3) #(i*i*i)
print(cube)


def cube(): #by using function
    result=[]
    for i in list:
        result.append(i*i*i)
    print(result)
list=[1,2,3,4]
cube()

#
def cube(n):
    res=[]
    for e in n:
        res.append(e**3)
    return res
n=[1,2]
x=cube(n)
print(x)

#E even or odd
even=[x for x in range(1,21) if x%2 ==0]
odds=[x for x in range(1,21) if x%2 !=0]
print('odds',odds,'even',even, end= ' ')


lst=[int(x) for x in input('enter').split(",")]
print(lst)
even=[]
odd=[]
for x in lst:
    if(x%2==0):
        even.append(x)
    else:
        odd.append(x)
print("Even list:",even)
print("odd list:",odd)  


#two line                         
obj=['even' if k%2==0 else 'odd' for k in range(20)]
print(list(enumerate(obj)))

#tuple or dict 
x=['even' if x%2==0 else 'odd'for x in range(1,11)]
print(tuple(enumerate(x)))


# one line 
print( [f"{i} is Even" if i%2==0 else f"{i} is odd" for i  in range(20)] )

#
print([f"{i} is even" if i %2==0 else
       f"{i} is odd" for i  in range(10)])

#P phone number check
p = []
q=[]
i = input("Enter Phone no:")
print( [f"{i} is right no" if len(i)==10  else f"{i} wrong no" ] )
if len(i)!=10:    
    p.append(i)
    print("inavlid No",p)
else :
    q.append(i)
    print("valid No",q)

#
pn=[]
for i in range(1):
        pn.append(input('Enter phone'))

correct=[i for i in pn if(len(i)==10)]
incorrect=[i for i in pn if(len(i)!=10)]
for i in incorrect:
    pn.remove(i)
print(correct)
print(incorrect)
print(pn)


#
print("enter numbers")
lst=[x for x in input().split(",")]
valid=[]
invalid=[]
for x in lst:
	if(len(x)==10):
		valid.append(x)
	else:
		invalid.append(x)
print("valid phonenum:",valid)
print("invalid invalid phonenum:",invalid)


#
mobile_nums = [input("Enter a mobile number : ") for i in range(2)]
print("User inputed mobile numbers :",mobile_nums)
correct_number = [i for i in mobile_nums if len(i) == 10]
print("Correct numbers ;",correct_number)
wrong_num = [i for i in mobile_nums if (len(i)!=10) ]
print("Wrong numbers : ",wrong_num)
for i in wrong_num:
    if i in mobile_nums:
        mobile_nums.remove(i)
print("Original list :",mobile_nums)

#
print("enter numbers")
lst=[x for x in input().split(",")]
print("original lst=",lst)
valid=[x for x in lst if(len(x)==10)]
invalid=[x for x in lst if(len(x)>10)or(len(x)<10)]
for x in invalid:
    lst.remove(x)
print("valid lists:",valid)
print("invalid lists:",invalid) 

#
ph=[x for x in input().split(",")]
cph=[]
wph=[]
count=0
for x in ph:
	if len(x)==10:
		cph.append(x)
		print("Correct phone number: ",cph)
else:
	ph.remove(x)
print("number removed from list: ",ph)


print("enter numbers")
lst=[x for x in input().split(",")]
print(lst)
correct=[]
incorrect=[]
ph_no=[correct.append(x) if(len(x)==10) else incorrect.append(x) for x in lst]
#print(ph_no)
for x in incorrect:
    if x in incorrect:
        lst.remove(x)
print("correct phone numbers:" ,correct)  
print("incorrect phone numbers:",incorrect)
print("removed incorrect numbers from the original list:", lst)

#error codes

l1=[x for x in input('enter values')]
ph=[]
count=0
for x in l1:
	count+=1 
	if count<=10:
		ph.append(x)
	else:
		l1.pop(x)
print("phone number: ",ph)
print("number removed from list: ",l1)  


num=input("enter phone number:")
if len(num)==10:
    if num[3]=='_' and num[7]=='_':
        if(num[:3]+num[4:7]+num[8:]).isdigit():
            print("phone number is valid")
else:
    print("phone number is invalid")

x=input('enter 10 digit number')
crrctno=[]
wrongno=[]
phn=[ crrctno.append(x) if len(x)==10 else wrongno.append(x)]
if phn is crrctno :
    print('crrctno',crrctno)
else:
    print('wrongno',wrongno)