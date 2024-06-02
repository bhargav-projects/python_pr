'''
Strong number is a special number 
whose sum of the factorial of digits 
equal to the original number
. For Example: 145 is strong number'''


n=145
temp,sum=n,0
while temp>0:
    res,fac=temp%10
    for x in range(res):
        fac*=x
    sum,temp=sum+fac,temp//10
print('yes' if sum==temp else 'no')


print('enter a number')
n=int(input())
temp,sum=n,0
while(n):
    i,f,r=1,1,n%10
    while i<=r:
        f,i=f*i,i+1
    sum,n=sum+f,n//10
print('yes' if sum==temp else 'no')

