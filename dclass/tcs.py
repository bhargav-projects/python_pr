  
#F factorial:
n=int(input())
fact=1
for i in range (1,n+1):
    fact=fact*i
print(" factorial of n is :",fact)

#G gcd of a and b   using Recursive function to return
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)
a,b=int(input('enter a ')),int(input('enter b '))
print(gcd(a,b))

#H  hcf method
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
a=int(input())
b=int(input())
print(hcf(a,b))

#L LCM of Two Numbers 
num1 = int(input())
num2 = int(input())
# Use If condition to find the greatest number among these two.
if(num1 > num2 ):   
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break;
    max= max+ 1

#L leap year or not
year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"  is leap year ")
        else :
            print(year, " is not leap year")
    else :
        print(year," is leap year ")
else :
    print(year," is  not leap year ")

#P palindrome or not
n=int(input())
rev=0
sum=0
temp=n

while n>0:
    r=n%10
    rev=rev*10+r
    sum+=1
    n=n//10
temp=sum
if sum==temp:
    print("p")
    
else :
    print(" f")


#P prime number is always greater than 1
n = eval(input("enter number "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("its not")
            break
    else:
        print(" it's prime number ")
else:
    print(" its not prime number")