'''in dict it arrange all equal values in one order
#set doesnt allow duplicates so counter is no useble but it executes
and in counter items return items are in descending order 
like more repeated elements are first 
'''

from collections import Counter

#list
l=[10,20,30,3,3,3,3,3,5,5,5]
print(Counter(l)) 


#str
from collections import Counter
s='hibhargav'
print(Counter(s))
print(type(s))  #str

#in dict it arrange all equal values in one order
# and set removes duplicates and 
from collections import Counter
s={1:'hibhargav',2:'bye',3:'hibhargav',4:'bye'}
print(Counter(s))
print(type(s))  #dict 

 
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# with keyword arguments
print(Counter(A=3, B=5, C=2))


l=[1,2,2,3,3,3,4,4,4,4,55]
print(Counter(l)) 
