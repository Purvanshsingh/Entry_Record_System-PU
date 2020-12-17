import sqlite3
import threading
import time
from Admin_login import *
from excel_export import *
from tkinter import messagebox
from tkinter import *
import datetime
import re
from openpyxl import load_workbook
def submit_entry(entry,e):
    global Person,Serial_number
    #Entry Clear
    e.delete(0,END)
    print(entry)
    print(Person.get())
    if str(Person.get())=='OTHERS':
        print("Others")
        Serial_number+=1
        time = datetime.datetime.now()
        data = (entry, time.strftime("%I:%M:%S %p"), str(Person.get()))
        listboxdata=(Serial_number,entry, time.strftime("%I:%M:%S %p"), str(Person.get()))
        create_excel_sheet(data)
        listbox.insert(0,listboxdata)
    else:
        collage_pattern = r"\d{4}(PU|pu)[a-z|A-Z]{7}\d{5}"
        try:
            check_vaild = re.match(collage_pattern, entry)
            print("here 2")
            if check_vaild is not None:
                    Serial_number += 1
                    time = datetime.datetime.now()
                    data = (entry, time.strftime("%I:%M:%S %p"),str(Person.get()))
                    listboxdata = (Serial_number, entry, time.strftime("%I:%M:%S %p"),str(Person.get()))
                    create_excel_sheet(data)
                    listbox.insert(0, listboxdata)
            else:
                raise Exception

        except Exception as e:
            print("NOT FOUND")
            messagebox.showerror("Warning","Invalid Registration No.")
def Get_College(data):
    college=data[:4]
    if 'PIET' in college:
        return 'PIET'
    elif 'PGI' in college:
        return 'PGI'
    else:
        return
def func(event):
    global v,Entry
    submit_entry(v.get(), Entry)
def year(data):

    x = data[:-5]
    y = x[-2:]
    print(y)
    try:
        year = 20 - int(y)
    except ValueError:
        return -999999
    else:
        if year == 1:
            return 'FIRSTYEAR'
        elif year == 2:
            return 'SECONDYEAR'
        elif year == 3:
            return 'THIRDYEAR'
        elif year == 4:
            return 'FOURTHYEAR'
#clock function
def Time():
    while True:
        clock_label['text']=time.ctime()
        time.sleep(1)
        if time.strftime("%H:%M:%S")=="09:30:00" or time.strftime("%H:%M:%S")=="12:00:00" or time.strftime("%H:%M:%S")=="14:30:00":
            print("Time verified")
            file=Get_Yesterday_File()
            if file:
                print("got file")
                Wb = load_workbook(file)
                sheet = Wb.active
                if sheet['C1'].value == None:
                    try:
                        Send_Data_To_Drive(file)
                    except ServerNotFoundError as e:
                        print(e,"1")
                        messagebox.showerror("ERROR","PLEASE CHECK YOUR INTERNET CONNECTION")
                    except Exception as e:
                        print(e)
                        messagebox.showerror("ERROR",e)
                    else:
                        sheet['C1'] = 'UPDATED'
                        Wb.save(filename=file)
                        messagebox.showinfo("SUCCESSFULL","BACKUP DONE")
                elif sheet['C1'].value == 'UPDATED':
                    print("Already updated")

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
background_img1=PhotoImage( file='main.png')
label=Label(window, image=background_img1)

#Welcome Label
Welcome_label=Label(label,text="Welcome To PU Library",bg='brown',fg='white', font=("Times 50 bold italic"),bd=5,relief=RAISED)
Welcome_label.pack(pady=10)
#Clock Frame
clock=Frame(label)
clock_label=Label(clock,bg='black',fg='red',padx=10,pady=10,font='Courier')
clock_label.pack()
clock.pack(pady=2)
time_thread=threading.Thread(target=Time,daemon=True)
time_thread.start()

#Entry box
entry_frame=Frame(label,height=800,width=100,bd=2)
frame_image=PhotoImage(file='final.png')
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
#Admin Login Button
Admin_login=Button(label,text="Admin Login",fg='white',bg='brown',font=("Courier 20 bold italic"),bd=4,relief=RAISED,command=lambda:login(window))
Admin_login.pack(side=RIGHT,padx=10,ipadx=5)
#Developed by
Developed_Label=Label(label,text='Developed By: PURVANSH SINGH (PIET18CS112)',fg='white',bg='black',bd=5,relief=RAISED,font='systemfixed 11')
Developed_Label.pack(side=LEFT,ipadx=5,ipady=5)
label.pack(expand=YES,fill=BOTH)
window.bind('<Return>', func)
window.mainloop()