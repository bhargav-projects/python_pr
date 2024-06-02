# threading synchronisation


''' The concept of allowing thread sequentially when these threads trying to access same resource parallel
 threading module is providing " lock " class to implement thread synchronisation

LOCK class is  providing predefined dynamic methods to lock SPECIFIC logic in the function
 .o=Lock()  # o is object
 .o.acquire()
 .o.release
     
we cant start multiple threads on the same  object '''

from threading import *
import time
class numbers:
    x=0 #static
    lock=Lock()
    def incrementx():                                    
        numbers.lock.acquire()
        numbers.x += 1
        numbers.lock.release()
        return
class custom1(Thread):
    def run(self):
        for i in range(100):
            numbers.incrementx()
        return
class custom2(Thread):
    def run(self):
        for i in range(100):
            numbers.incrementx()
        return
class default:
    n=0
    def main():
        o1=custom1()
        o2=custom2()

        o1.start()
        o2.start()
        
        o1.join()
        
        o2.join()
        print("final value is :"+str(numbers.x))
        return
default.main()