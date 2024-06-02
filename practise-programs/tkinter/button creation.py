from tkinter import * 
root=Tk()                   # heare instead of root u can choose any varibale
root.title('gui')           #select title for ur  root 
root.geometry('500x300')    # dimensions of root
def fun():
    print('welcome to GUI')  
    return
    
# b=Button(root,text='click me',command=fun)
# b.pack()                    # pack used to fit the  text in Button

b=Button(root,text='click me',command=fun,fg='white',bg='green')
#b.place(x=200,y=100)
b.pack()
