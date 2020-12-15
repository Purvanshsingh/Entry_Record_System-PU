from tkinter import *
from tkinter import ttk,messagebox
from tkinter.filedialog import askopenfile
from sqlite3 import OperationalError
import sqlite3
import pandas as pd
from GoogleDriveApi import Authentication
import os
import time
def Import_data():
    global Year,College_var
    global var
     # IMPORT DATA FROM EXCEL TO DB
    Year = var.get()
    College=College_var.get()
    conn = sqlite3.connect(str(College)+'.db')
    file = askopenfile(mode='r',title = "Select file",filetypes = (("Excel files","*.xls"),("all files","*.*")))
    try:
        p = pd.read_excel(file.name)
        p.to_sql(Year, conn, index=False, if_exists='replace')
    except Exception as e:
        print(e)
    else:
        messagebox.showinfo("SUCCESSFULL","DATA IMPORTED")
        print("Done")
        conn.commit()
        conn.close()
def Connection(college):
    global Year
    global cursor
    try:
        conn = sqlite3.connect(str(college)+'.db')
    except Exception as e:
        messagebox.showerror("ERROR SOMETHING WENT WRONG")
    else:
        print("Connection establised")
        try:
            cursor = conn.execute("SELECT registration_number from " + Year)
            return True
        except OperationalError as e:
            messagebox.showwarning("ERROR",e)
            return None
def Search():
    global Year,Details
    global var,College_var
    global cursor
    Details.delete(0,END)
    Year=var.get()
    if Connection(str(College_var.get())):
        for i in cursor:
            Details.insert(0,i[0])
def Auth():
    try:
        os.remove("token.pickle")
        time.sleep(3)
    except Exception as e:
        print(e)
        time.sleep(3)
    finally:
        Authentication()
def Dashboard():
    global College_var
    global var
    global Year
    global Details
    root =Tk()
    root.title("DASHBOARD")
    root.config(bg='#191970')
    root.geometry('1500x700+0+0')
    Dashboard_label=Label(root,text='DASHBOARD',bg='black',fg='#FFB319', font=("Times 40 bold italic"),bd=5,relief=GROOVE)
    Dashboard_label.grid(row=0,columnspan=5,ipadx=50)
    Registration_label=Label(root,text='Enter regitration number',bg='#00BFFF')
    Registration_no=Entry()
    College_var=StringVar()
    var = StringVar()
    Year = 'FIRSTYEAR'
    #Buttons
    search=Button(root,text='Search',bg='#FFB319',activebackground='green',activeforeground='white',bd=5,relief=RAISED,command=Search)
    Details=Listbox(width=250,height=30)
    New_Records=Button(root,text="Add New Records",bg='#FFB319',activebackground='green',activeforeground='white',bd=5,relief=RAISED,command=Import_data)
    edit=Button(root,text="Edit Records",bg='#FFB319',activebackground='green',activeforeground='white',bd=5,relief=RAISED)
    #select year
    Select_label=Label(text='Select Year',bg='#00BFFF')
    Year=['FIRSTYEAR','SECONDYEAR','THIRDYEAR','FOURTHYEAR']
    selection=ttk.Combobox(root,values=Year,textvariable=var,justify=CENTER,state='readonly')
    selection.current(0)
    #Select Year
    # select year
    Select_College_label = Label(text='Select College', bg='#00BFFF')
    college = ['PIET', 'PGI']
    selection_college= ttk.Combobox(root, values=college, textvariable=College_var, justify=CENTER, state='readonly')
    selection_college.current(0)
    #Set Google Drive ID
    Set_GoogleDrive_Authentication=Button(root,text='Google Drive Authentication',bg='#FFB319',activebackground='green',activeforeground='white',bd=5,relief=RAISED,command=Auth)
    #Grid
    Registration_label.grid(row=2,column=0,ipadx=64,ipady=10)
    Registration_no.grid(ipadx=50,ipady=10,row=2,column=1,padx=20)
    Set_GoogleDrive_Authentication.grid(row=3,column=4,ipady=10,pady=10,padx=5)
    search.grid(ipadx=55,ipady=10,row=1,column=4)
    Select_label.grid(row=1,column=0,ipadx=100,ipady=10)
    selection.grid(row=1,column=1,ipadx=40,ipady=10)
    Select_College_label.grid(row=1,column=2,ipadx=80,ipady=10)
    selection_college.grid(row=1,column=3,ipadx=40,ipady=10,padx=30)
    Details.grid(row=3,column=0,columnspan=4,rowspan=3,padx=20,pady=10)
    New_Records.grid(ipadx=25,ipady=10,row=4,column=4,padx=5)
    edit.grid(ipadx=40,ipady=10,row=5,column=4,pady=5,padx=5)
    for i in range(3):
        root.grid_rowconfigure(i,weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.mainloop()
if __name__=='__main__':
    Dashboard()