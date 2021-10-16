''' WE CAN ACCESS LOCAL VARIABLES BY ACCESSING THIER RESPECTIVE CLASSES '''
from threading import *
import time
class custom1(Thread):
    res=0 #static
    def run(self):
        for i in range(1,default.n+1):
            custom1.res +=i   # HERE WE ADD CLASS AS WELL AS VAR AND MAKE NEW VARIABLE 
        return
class default:
    n=0
    def main():
        default.n=int(input('enter number '))   # HERE WE ADD CLASS AS WELL AS VAR AND MAKE NEW VARIABLE 
        o1=custom1()
        o1.start()
        
        o1.join()
        print(' res is:'+str(custom1.res))
        return
default.main()