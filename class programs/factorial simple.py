n=int(input('enter num'))
res=1
for i in range(1,n+1):
    res*=i
   #print(res) ( if we place print here we get every multiple value)
print(res)

#while 
n=int(input('enter number '))
res=1
i=1
while i<n+1:
    res*=i
    i+=1
print('factorial sum of ',n,'is',res)

#using def 
def fact(n):
    res=1
    while n>=1:
        res*=n
        n=n-1
    return res
     
n=int(input(' enter  number'))

print(fact(n))

#factorila for in range:
def fact(n):
    res=1
    while n>=1:
        res*=n
        n=n-1
    return res
     
for k in range(1,6):
    print('the factorial of ',k,'is',fact(k))

# 3 ways of calling fun as i know
def factorial(n):
  res=1
  k=1
  while k<n+1:
    res*=k
    k=k+1
  return res


# type 1 of calling
print(factorial(3)) 

# type 2 of calling
n=factorial(5) 
print(n)

#type 3 of calling
for n in range(1,6):
    print('the factorial of ',n,'is',factorial(n))

# Recursion
#factorial using recursion 
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(5))




