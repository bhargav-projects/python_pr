class demo:
    file=None
    def main():
        try:
            demo.file=open("p.py","r")
            print('file opened')
            data=demo.file.read()
            count=0
            for sym in data:
                print(sym, end=' ')
                count +=1
            print('number of symbols is:',count)

        except Exception as e:
            print(e)
        finally:
            if demo.file !=None:

                demo.file.close()
                print('file closed')
        return
demo.main()
