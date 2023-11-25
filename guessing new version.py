n=-1
import random
q=random.randint(0,200)
while True:
 from tkinter import*
 import tkinter.messagebox as tmsg
 root=Tk()
 
 def ff():
    quit()
 def best():
    v= xentry.get()
    if int(v)==int(q):
        
        b=tmsg.showinfo('info','you guessed it right') 
        rot=Tk()
        def dd():
            global n
            rot.destroy()
            n=-1
            root.destroy()
               
        rot.geometry('400x200')
        rot.title('choose')
        f=Frame(rot)
        f.grid(row=0)
        Label(f,text='DO YOU WANT TO PLAY AGAIN',font=('comicsansms',19,'bold')).grid()
        Button(rot,text='YES',command=dd,fg='red',bg='yellow',padx=110,pady=25).grid(row=1)
        Button(rot,text='NO',command=ff,fg='red',bg='yellow',padx=110,pady=25).grid(row=2)

        rot.mainloop
    elif int(v)>int(q):
        tmsg.showinfo('info','you have to guess lesser ')
        
        root.destroy()
    elif int(v)<int(q):
        tmsg.showinfo('info','you have to guess greater ')
        root.destroy()
 
 n=n+1

 if n==13:
    tmsg.showinfo('info','you used all of your 12 chances')
    quit()

 label=Label(root,text=f'you used {n} chances out of 12',font=('comicsansms',10,'bold')).grid(row=2,column=1)

 root.geometry('480x150')
 root.title('title')
 
 Label(text='You have to guess a number which is in between 0 to 200',font=('comicsansms',8,'bold'),fg='blue').grid(row=0,column=1)
 Label(text='Guess',font=('comicsansms',19,'bold'),fg='green').grid(row=1,column=0)
 x=StringVar()
 xentry=Entry(textvariable=x,border=10,fg='red',bg='purple')
 xentry.grid(row=1,column=1)

 Button(text='check',command=best,font=('comicsansms',15,'bold'),fg='blue',bg='grey').grid(row=3,column=1,padx=12,pady=8)
 print('ok')
 root.mainloop()

