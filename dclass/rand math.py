'''
 'Random','_Sequence', '_Set', '__all__', '__builtins__', 
 __cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', '_accumulate', '_acos', '_bisect',
'_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os', 
'_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test',
'_test_generator', '_urandom', '_warn', 'betavariate', 'choice',
'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits',
'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 
'randbytes', 'randint', 'random', 'randrange'
'''
from math import *
from typing import Sequence # *takes every thing but it takes more item
#print(cos(30))
#print(sin(30))
#print(sqrt(25))
#print((ceil(10.1)))
#print((floor(10.1)))
#print(fabs(-10.6))  # changing sign given sign to positive 
#print(fabs(-10.6))

#to generate random numbers 
from random import *
for k in range(10):
    print(random()) #b/n 0 and 1 

#for random int  values 
#rand int generate int values in given rannge #inclusive 
from random import *
for k in range(10):
    print(randint(1,100)) # b/n 1,100

#for random float values 
#uniform genarates float values in given range  # not inclusive
from random import *
for k in range(10):
    print(uniform(1,10))  # there is no 1 and 10 in res  ,becze  both are exclusive 

 
from random import *
#it give rand values range including 1to
for k in range(10):
    print(randrange(10),end=' ') 
    print(randrange(1,10),end=' ')
    print(randrange(1,10,2),end=' ')

# choice takes ANY indexable sequence (lis,tuple,str,dict) not set
from random import *
l=['hi','bhragav','how r u ']
print(choice(l))

#6digit pas 
from random import *
for k in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

#
from random import *
for i  in range(10):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9))



#beacuse it starts with 100000 # not a recoomende 
from random import *
for k in range(10):
    print(randint(100000,999999))





#print(randrange(1,9,2))
#print(randint(1,9))
#print(randbytes(1))
#l=(1,2,3,4)
#print(choice(l))
#print(choices(l))
#print(Sequence(l))