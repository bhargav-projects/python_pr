class demo:
    file=None
    def main():
        try:
            demo.file=open("practise.py","r") #if we perform write mode all data will be erased and new data will create
            print('file opened')
            data=demo.file.read()
            print(data)
        except Exception as e:
            print(e)
        finally:
            if demo.file !=None:  

                demo.file.close()
                print('file closed')
        return
demo.main()

