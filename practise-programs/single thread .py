
class numbers:
    def display(self):
        for i in range(50):
            print(i)
            return
class default:
    
    def main():
        print('starts @ main')
        obj=numbers()
        obj.display()
        for j in range(50):
            print(j)
        print('ends @ main')
        return
default.main()

