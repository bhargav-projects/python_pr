from threading import *
import time
class custom(Thread):
    def display(self):
        for i in range(1,11):
            print('custom:'+str(i))
            time.sleep(1)

        return
class default:
    def main():
        o=custom()
        o.display()
        for j in range(20):
            print('default:'+str(j))
            time.sleep(1)
        return
default.main()