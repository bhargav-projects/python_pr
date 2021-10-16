 #in str parethesis is optional
#eval()  = eval must require str argument other wise it gives error


# beacause it cant evalute int inside str directly
x=eval(input('10+3'))  #enter number ==> 10+3=13
print(x)

#type3
z=eval(input(10+3))  #19
print(z)

#type2
y=eval('10+3')   #19
print(y)


#type4
for x in range(4):
    ex=input('enter anyexpression')
    res=eval(ex)
    print(type(res))
    
#converting type casting from input
l=eval(input('list'))
t=eval(input('tuple'))  # 'n',9 # ('b',9)
s=eval(input('set'))
d=eval(input('dic'))
sr=eval(input('str'))   #'n' # ('b')
# with in the "quotations" what ever u write is string 
#by mistake if u write some thing after ("quotations",'like') this is is
#tuple 
print(type(l),type(t),type(s),type(d),type(sr))
print(l,t,s,d,sr)
