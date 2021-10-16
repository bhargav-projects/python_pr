import csv
class demo:
    src=None
    def main():
        try:
            demo.src=open('demo.csv','r')
            csv_reader=csv.reader(demo.src)
            for record in csv_reader:
                print(record)
        except Exception as e:
            print(e)
        finally :
            if demo.src !=None:
                demo.src.close()
                print('src closed')
            return
demo.main()
                
##  cs table data read 

import csv
from os import close
class demo:
    
    file=None
    def main():
        try:
            demo.file=open('source.csv','r')
            print('file opened')

            table=csv.reader(demo.file)
            for record in table:
                print(record)
        except Exception as e:
            print('exception',e)
        finally:
            if demo.file !=None:

                demo.file.close()
                print('file closed')
        return
demo.main()
