
class demo:
    src=None
    dst=None
    def main():
        try:
            demo.src=open("practise.py","r")
            demo.dst=open("f.txt","w")
            print('file opened')
            data=demo.src.read()
            for sym in data:
                demo.dst.write(sym)
            print('copied successfully')
        except Exception as e:
            print(e)
        finally:
            if demo.src !=None:

                demo.src.close()
                print('file closed')
        return
demo.main()
