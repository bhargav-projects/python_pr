#positional arguments 
def add(a,b):
    print(a,b)
add(4,5)

#keyword arguments 
def add(a,b):
    print(a,b)
add(2,b=7) 
#but here i given b is 7 in calling so it changes default to calling value  
#add(b=7,a) #it gives error because a is positional argument
# and it should be in first always 

#default arguments 
def add(b,a='hi'):
    print(a,b)
add('bhargav','how')
add('its b')  #here u can see that im not giving a value but its printed 

#keyword argument should contain in last only 

#varible length arguments
#def sum(*n): #here n means tuple
#wap to sum of n numbers 
def sum(*n):  # (*)means n no of values  
    result=0
    for x in n:
        result+=x
    print(result)

sum()
sum(10)
sum(10,20)
sum(10,20,30)
#type1
def sum(name,*n):
    result=0
    for x in n:
        result+=x
    print('the sum by',name,':',result)

sum('traca')
sum('traca',10)
sum('traca',10,20)
sum('traca',10,20,30)

#type2
def sum(*n,name):
    result=0
    for x in n:
        result+=x
    print('the sum by',name,':',result)

sum(10,name='traca')
sum(10,20,name='traca')
sum(10,20,30,name='traca')

# (**kwargs) means n nof keyword arguments
# def sum(**n): # it will become dictionary
def kwargs2(**dictype):
    print('we are printing dict type values by using function')
    for j,k in dictype.items():
        print(j,'...',k)
kwargs2(name='bhargav',num=100)

def display(**kwargsd):
    print('record info')
    for k,v in kwargsd.items():
        print(k,'....',v)
display(name='bhargav',marks=100,age= 20)
display(name='bhargav',wife1='queen',wife3= "queen2")
# it giving error because keys are same
# display(nae='bhargav',marks=100,age= 20,nam='bharga',wife1='queen',wife3= "queen2")

