class a:
    def m1(self):
        print("a- m1")
class b(a):
    pass    # instead of pass we can use "..."
class c:
    def m1(self):
        print("c- m1")
    def m2(self):   
        print("c- m2")
class d(a,c):
    def m2(self):
        print("d-m2")
    def m3(self):
        print("d-m3")
class inheritance:
    def main():
        o=b()
        o.m1()
        o=d()
        o.m1()
inheritance.main()
