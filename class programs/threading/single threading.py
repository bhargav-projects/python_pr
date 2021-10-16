from threading import *
class custom(Thread):
    def display(self):
        for i in range(20):
            print('custom:'+str(i))
        return
class default:
    def main():
        o=custom()
        o.display()
        for j in range(20):
            print('default:'+str(j))
        return
default.main()