'''

'''

# by using math Module
from math import pow
x = [int(pow(i,3)) for i in range(0,5)]

#two line                         
obj=['even' if k%2==0 else 'odd' for k in range(20)]
print(list(enumerate(obj)))

print([f"{i} is even" if i %2==0 else
       f"{i} is odd" for i  in range(10)])
 