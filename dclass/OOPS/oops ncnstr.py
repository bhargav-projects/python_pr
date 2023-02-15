#WITHOUT CONSTRUCTOR 
#accessing instance varibles without constructor
#outside of the class by using object 
class Movie:
    def inf(s):
        print('movie name',s.na)
        print('movie hero',s.h)
        print('movie heroin',s.hi)
        print('movie rating',s.ra)   
        print()


obj=Movie()
obj.na='bahu'
obj.h='prabha'
obj.hi='anushk'
obj.ra=10
obj.inf()

#type 2
#inside instance method by using self varible 
class nocnstruct:
    def nc(self,name,num,rating):
        self.name=name
        self.num=num
        self.rating=rating
    def info(self):
        print(self.name)
        print(self.num)
        print(self.rating)
       
s=nocnstruct()
s.nc('abc',2,3)
s.info()
#s=nocnstruct('abc',2,3)   #giving error