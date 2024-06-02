
# sender is the responsible to save employee object file
import pickle
from emp  import *

f= open("emp.dat","wb")
while True:
    eno=int(input(' enter employee number'))
    ename=input(' enter name')
    esal=float(' enter salary')
    eadres=input(' enter adress')
    e=Employee(eno,ename,esal,eadres)
    pickle.dump(e)
    option=input('do you want to  serilize one more emp object : [Yes|No')
    if option.lower() =='No':
        break
print(' all employe objects serialised')