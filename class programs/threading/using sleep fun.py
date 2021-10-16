'''run() is pre defined thread class with empty defintion
start()  method allocates separate thread space to executes run() method logic parallel 
run() method over ride by the programmer with custom thread logic 
'''
from threading import *
import time
class custom1(Thread):
    def run(self):
        for i in range(1,11):
            print('custom:'+str(i))
            time.sleep(1)

class custom2(Thread):
    def run(self):
        for i in range(50,71):
            print('custom2:'+str(i))
            time.sleep(2)

class custom3(Thread):
    def run(self):
        for i in range(100,90,-1):
            print('custom3:'+str(i))
            time.sleep(3)
        return
class default:
    def main():
        o1=custom1()
        o1.start()
        
        o2=custom2()
        o2.start()
        
        o3=custom3()
        o3.start()
        return
default.main()