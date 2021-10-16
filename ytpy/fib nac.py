
#type 2 for within range 
n=int(input('number'))
a=1
b=0
for k in range(0,n):
    c=b
    b=a
    a=c+b
    print(a)

# #using gen
def fib(): 
    a,b=0,1 
    while True: 
       yield a 
       print(a,end=' ')
       a,b=b,a+b 
for f in fib(): 
    if f>100: 
        break  
print(f) 