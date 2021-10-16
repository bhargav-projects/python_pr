#factors of a number
n=int(input(" hey radhe give a number:"))
for i in range(1,n):
    if n%i==0:
        print("factors of ",n,"is",i,)

#factors of a number using while 
n=int(input(" hey radhe give a number:"))
i=1
while i<n:
    if n%i==0:
        print('factors of ',n,'is',i)
    i=i+1
    
#factors of a number using while 
n=int(input(" hey radhe give a number:"))
i=1
x=[i for i in range(1,n) if n%i==0]
print(x)

