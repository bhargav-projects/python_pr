from tkinter import *    # * means u are importing everything in tkinter
def display():
    name=e.get()
    print('hello'+name+'welcome to tkinter')  
    return
root=Tk()                   # heare instead of root u can choose any varibale
root.title('gui')           #select title for ur  root 
root.geometry('900x400')    # dimensions of root

l=Label(root,text='enter name',font='arial 30')
l.place(x=300,y=100)

e=Entry(root,font='ariel 30')
e.place(x=300,y=100)
    
b=Button(root,text='diplay',command=display,fg='white',bg='green')
b.place(x=800,y=100)        #   fit the button in custom position

