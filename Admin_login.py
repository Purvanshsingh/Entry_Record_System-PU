from tkinter import *
from tkinter import messagebox
import Dashboard
def validate(window,w,namevar,passvar):
    print("here")
    if namevar=='admin' and passvar=='root':
        print("logged in")
        w.destroy()
        Dashboard.Dashboard()
    else:
        messagebox.showerror("Warning","Incorrect Username or Password")
        window.destroy()
        login(w)

def login(w):
    window=Toplevel()
    window.title('ADMIN LOGIN')
    window.maxsize(400,400)
    window.geometry('400x400+500+100')
    background_img=PhotoImage(file='login.png')
    main_frame=Frame(window)
    main_label=Label(main_frame,image=background_img,bd=2)
    '''LOGIN_LABEL=Label(main_label,text='ADMIN LOGIN',bg='orange',fg='black',font=("Courier 30 italic"),relief=RAISED)
    LOGIN_LABEL.pack(expand=YES,fill=X,padx=5,pady=5)'''
    namevar=StringVar()
    passvar=StringVar()
    Name=Label(main_label,text='ENTER YOUR NAME:',bg='black',fg='light blue',relief=RAISED)
    Name_entry=Entry(main_label,bd=5,textvariable=namevar)
    Password=Label(main_label,text='ENTER PASSWORD:',bg='black',fg='light blue',bd=2,relief=RAISED)
    Password_entry=Entry(main_label,bd=5,show='*',textvariable=passvar)
    print("hello")
    Login=Button(main_label,text='LOGIN',bg='light blue',fg='black',font=("Courier 25 italic"),relief=RAISED,bd=5,
                 command=lambda:validate(window,w,namevar.get(),passvar.get()))
    Name.pack(expand=YES,fill=X,padx=10,pady=10,ipady=10)
    Name_entry.pack(expand=YES,fill=X,padx=30,pady=10,ipadx=5,ipady=5)
    Password.pack(expand=YES,fill=X,padx=10,pady=10,ipady=10)
    Password_entry.pack(expand=YES,fill=X,padx=30,pady=10,ipadx=5,ipady=5)
    Login.pack(expand=YES,fill=X,padx=10,pady=10)
    main_label.pack(expand=YES,fill=BOTH)
    main_frame.pack(expand=YES,fill=BOTH)
    window.mainloop()