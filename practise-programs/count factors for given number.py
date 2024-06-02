# count no of factors for given number
def factors(n):
    k=0 #count the factors
    for i in range (1,n):
        if n%i==0:
            k=k+1      # k+=1
    return k
n=int(input('enter number'))   # instead of int we can use eval()
k=factors(n)
print("factors of n is:",k)

# using While loop 
n=eval(input('enter number'))
count=0
i=1
while i<n:
    if n%i==0:
        count+=1
    i+=1
print(count)

# using list comprehension
n=int(input(''))
x=[int(k) for k in range(1,n) if n%k==0 ]
print(x)
