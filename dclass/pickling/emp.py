
import pickle
class Employee:
    def __init__(self,ename,eno,esal,eadres):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadres=e0adres
    

    def display(self):    
    
     print('ENAME{},ENO{},ESAL{},EADRESS{}'.format(self.ename,self.eno,self.esal,self.eadres))

e=Employee('bhargav',2,999999,'vgmbpm')
with open ('pickle.dat',"wb") as f:
    pickle.dump(e,f)
    print(' pickling employee data succcessfully')

with open ('pickle.dat',"rb") as f:
    obj=pickle.load(f)
    print('unpickling complted ')
    print('printing employee inf ')
    obj.display() 

    