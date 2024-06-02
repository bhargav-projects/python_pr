'''a perfect number is a positive integer
 that is equal to the sum of its positive divisors
 , excluding the number itself.
  For instance,
   6 has divisors 1, 2 and 3 (excluding itself),
 and 1 + 2 + 3 = 6, so 6 is a perfect number.'''


#type 2
nfactor_sum,n=0,6
for x in range(1,n):
    if n%x==0:
        print(x)
        nfactor_sum+=x
print('its perfect number' if n==nfactor_sum else 'not perfectnumber')
    
#with in range
def perfect(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum=sum+x
    return (True if sum==n else False)
for n in range(1,1000):
    if perfect(n): print(n)

#type2     
def print_perfect_nums(start, end):
    for i in range(start, end + 1):
        sum1 = 0
        for x in range(1, i):
            if(i % x == 0):
                sum1 = sum1 + x
                if (sum1 ==i):
                    print(i)
print_perfect_nums(1, 300)

#

for i in range(10, 101):
    sum1 = 0
    for x in range(1, i):
      # Check if a divisor, if it is, add to sum
        if(i % x == 0):
            sum1 = sum1 + x
            if (sum1 == i):
                print(i)