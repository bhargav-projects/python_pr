class emp:
    def __init__ (self,num,name):
        self.num=num
        self.name=name
        return
    def details(self):
        print(" emp num is ",self.num)
        print(" emp name is ",self.name)
        return
class access:
    def main():
        print(" enter emp details")
        name=input("enter name")
        num=int(input('enter num'))
        
        obj=emp(num,name)
        obj.details()
        return

access.main()
