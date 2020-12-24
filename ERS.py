from threading import Thread
from time import strftime, ctime, sleep
from excel_export import *
from tkinter import messagebox
from tkinter import *
from datetime import datetime
from re import match
from openpyxl import load_workbook
import os
def submit_entry(entry,e):
    global Person,Serial_number
    #Entry Clear
    e.delete(0,END)
    if str(Person.get())=='OTHERS':
        Serial_number+=1
        time = datetime.now()
        data = (entry, strftime("%I:%M:%S %p"), str(Person.get()))
        listboxdata=(Serial_number,entry, strftime("%I:%M:%S %p"), str(Person.get()))
        create_excel_sheet(data)
        listbox.insert(0,listboxdata)
        Person.set("STUDENTS")
    else:
        collage_pattern = r"\d{4}(PU|pu)[a-z|A-Z]{7}\d{5}"
        try:
            check_vaild = match(collage_pattern, entry)
            if check_vaild is not None:
                    Serial_number += 1
                    time = datetime.now()
                    data = (entry, strftime("%I:%M:%S %p"),str(Person.get()))
                    listboxdata = (Serial_number, entry, strftime("%I:%M:%S %p"),str(Person.get()))
                    create_excel_sheet(data)
                    listbox.insert(0, listboxdata)
            else:
                raise Exception

        except Exception as e:
            messagebox.showerror("Warning","Invalid Registration No.")

def func(event):
    global v,Entry
    submit_entry(v.get(), Entry)
#clock function
def Time():
    while True:
        clock_label['text']= ctime()
        sleep(1)

def enter(event):
    submit['bg']='green'
    submit['fg']='white'
def leave(event):
    submit['bg']='white'
    submit['fg'] = 'black'
Serial_number=0
window=Tk()
window.geometry('1280x1024')
window.title("ENTRY_RECORD_SYSTEM")
background_img1=PhotoImage(file= os.path.abspath("picture\\main.png"))
label=Label(window, image=background_img1)

#Welcome Label
Welcome_label=Label(label,text="Welcome To PU Library",bg='brown',fg='white', font=("Times 50 bold italic"),bd=5,relief=RAISED)
Welcome_label.pack(pady=10)
#Clock Frame
clock=Frame(label)
clock_label=Label(clock,bg='black',fg='red',padx=10,pady=10,font='Courier')
clock_label.pack()
clock.pack(pady=2)
time_thread= Thread(target=Time,daemon=True)
time_thread.start()

#Entry box
entry_frame=Frame(label,height=800,width=100,bd=2)
frame_image=PhotoImage(file=os.path.abspath("picture\\final.png"))
entry_label=Label(entry_frame,image=frame_image,height=800,width=100,bd=5)
enter_here=Label(entry_label,text="ENTER YOUR REGISTRATION NO:",fg='white',bg='black',bd=5,relief=RAISED,font='Courier')
v=StringVar()
Person=StringVar()
#Students and Others
Students=Radiobutton(entry_label,text='PU STUDENTS',variable=Person,value='STUDENTS',bd=3,relief=RAISED)
OTHER=Radiobutton(entry_label,text='OTHERS',variable=Person,value='OTHERS',bd=3,relief=RAISED)
Person.set('STUDENTS')
Entry=Entry(entry_label,font=('Times', 20, 'bold'),textvariable=v)
submit=Button(entry_label,text='Submit',relief=RAISED,bd=5, command=lambda:submit_entry(v.get(),Entry))
#Submit Button Bind
submit.bind('<Enter>',enter)
submit.bind('<Leave>',leave)
listbox=Listbox(entry_label)

Students.grid(row=1,column=0,pady=5,ipadx=20,padx=20)
OTHER.grid(row=1,column=2,pady=5,ipadx=25,padx=20)
listbox.grid(row=4,padx=20,pady=20,ipadx=20,ipady=10,columnspan=3)
submit.grid(row=3,pady=20,ipadx=10,columnspan=3)
Entry.grid(row=2,padx=10,pady=10,columnspan=3,ipadx=5)
enter_here.grid(row=0,padx=5,pady=35,ipadx=20,ipady=20,columnspan=3)
entry_label.pack(expand=YES,fill=BOTH)
entry_frame.pack(expand=YES,fill=Y,pady=10)
#Developed by
Developed_Label=Label(label,text='Developed By: PURVANSH SINGH (PIET18CS112)',fg='white',bg='black',bd=5,relief=RAISED,font='systemfixed 11')
Developed_Label.pack(side=LEFT,ipadx=5,ipady=5)
label.pack(expand=YES,fill=BOTH)
window.bind('<Return>', func)
window.mainloop()