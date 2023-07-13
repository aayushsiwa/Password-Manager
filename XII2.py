import tkinter as tk
import mysql.connector as m
from mysql.connector import errorcode
import sys
import tkinter.font as tkFont
import time
from ende import encode
from ende import decode
import os
import string
import random

bg = "#ff5722"
fg = "#ffffff"
rf = "groove"
jf = "center"


fname='Details.txt'
# Function for calculation of password

def read(fname):
    global l
    f=open(fname,'r')
    l=f.readlines()

read(fname)
r=l[0]
try:
        cnx = m.connect(user=decode(r,l[1]),password=decode(r,l[2]))
        #print('Connected to MySql')
except m.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
os.remove(fname)
#os.remove(fname2)

cursor=cnx.cursor()

databases=[]

cursor.execute('SHOW DATABASES')

for i in cursor:
    databases.append(i[0])

DATABASE='passwordmanager'

if 'passwordmanager' in databases:
    cnx.close()
else:
    cursor.execute(f'CREATE database {DATABASE}')
    cnx.close()

cnx=m.connect(user=decode(r,l[1]),password=decode(r,l[2]),database=f'{DATABASE}')

cursor=cnx.cursor()

cursor.execute('SHOW TABLES')

tables=[]

for i in cursor:
    tables.append(i[0])
if 'passwords' not in tables:
    cursor.execute('create table passwords(website char(120) not null, username char(120) not null, password char(120) not null)')

def __init__3():
    global GLineEdit_520
    global root
    global var
    root=tk.Tk()
    #setting title
    root.title("undefined")
    root.attributes('-alpha',0.9)
    root["background"] = "#ff5722"      
    #setting window size
    width=834
    height=156
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    ft = tkFont.Font(family='Times',size=20)
    ft2 = tkFont.Font(family='Times',size=14)
    root.resizable(width=False, height=False)

    GLabel_408=tk.Label(root)
    GLabel_408["bg"] = "#ff3d00"
    GLabel_408["font"] = ft
    GLabel_408["fg"] = fg
    GLabel_408["justify"] = jf
    GLabel_408["text"] = "Generate Password"
    GLabel_408["relief"] = "raised"
    GLabel_408.place(x=0,y=0,width=834,height=42)

    GLabel_41=tk.Label(root)
    GLabel_41["bg"] = bg
    GLabel_41["font"] = ft
    GLabel_41["fg"] = fg
    GLabel_41["justify"] = jf
    GLabel_41["text"] = "Password"
    GLabel_41.place(x=0,y=60,width=417,height=42)

    GLineEdit_520=tk.Entry(root)
    GLineEdit_520["bg"] = bg
    GLineEdit_520["borderwidth"] = "5px"
    GLineEdit_520["font"] = ft
    GLineEdit_520["fg"] = fg
    GLineEdit_520["justify"] = jf
    GLineEdit_520["text"] = "Entry"
    GLineEdit_520.place(x=417,y=60,width=417,height=42)

    GButton_151=tk.Button(root)
    GButton_151["bg"] = bg
    GButton_151["font"] = ft2
    GButton_151["fg"] = fg
    GButton_151["justify"] = jf
    GButton_151["text"] = "Copy"
    GButton_151["relief"] = rf
    GButton_151.place(x=208.5,y=120,width=208.5,height=42)
    GButton_151["command"] = GButton_151_command

    GButton_166=tk.Button(root)
    GButton_166["bg"] = bg
    GButton_166["font"] = ft2
    GButton_166["fg"] = fg
    GButton_166["justify"] = jf
    GButton_166["text"] = "Cancel"
    GButton_166["relief"] = rf
    GButton_166.place(x=650,y=120,width=208.5,height=42)
    GButton_166["command"] = GButton_166_command

    GButton_758=tk.Button(root)
    GButton_758["bg"] = bg
    GButton_758["font"] = ft2
    GButton_758["fg"] = fg
    GButton_758["justify"] = jf
    GButton_758["text"] = "Generate"
    GButton_758["relief"] = rf
    GButton_758.place(x=0,y=120,width=208.5,height=42)
    GButton_758["command"] = GButton_758_command

    GLabel_517=tk.Label(root)
    GLabel_517["bg"] = bg
    GLabel_517["font"] = ft
    GLabel_517["fg"] = fg
    GLabel_517["justify"] = jf
    GLabel_517["text"] = "Length"
    GLabel_517.place(x=417,y=120,width=208.5,height=42)


    values=[8,9,10,11,12,13,14,15,16,17,18]
    var=tk.IntVar(root)
    var.set(8)
    GListBox_855=tk.OptionMenu(root,var,*values)
    GListBox_855["bg"] = bg
    GListBox_855["borderwidth"] = "1px"
    GListBox_855["font"] = ft2
    GListBox_855["fg"] = fg
    GListBox_855["justify"] = jf
    GListBox_855["relief"] = "sunken"
    GListBox_855.place(x=560,y=130,width=80,height=25)
    GListBox_855["activebackground"] = bg

    root.mainloop()
       

def GButton_151_command():
    random_password = GLineEdit_520.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)


def GButton_166_command():
    root.destroy()


def pswd():
    GLineEdit_520.delete(0, tk.END)
    GLineEdit_708.delete(0,tk.END)
    # Get the length of passowrd
    length = int(var.get())
    print(int(var.get()))
    digits =string.punctuation+string.digits+string.ascii_lowercase+string.ascii_lowercase
    password = ""
    for i in range(0,length):
        password+=random.choice(digits)
    return password


def GButton_758_command():
    a=pswd()
    GLineEdit_520.insert(10,a)
    GLineEdit_708.insert(10,a)



def __init__1():
    global root1
    global ft
    global ft2
    global GLineEdit_708
    global GLineEdit_185
    global GLineEdit_800
    root1=tk.Tk()
    root1.title("PasswordManager")
    root1.attributes('-alpha',0.9)
    root1["background"] = bg
    width=834
    height=340
    screenwidth = root1.winfo_screenwidth()
    screenheight = root1.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root1.geometry(alignstr)
    root1.resizable(width=False, height=False)
    ft = tkFont.Font(family='Times',size=22)
    ft2 = tkFont.Font(family='Times',size=14)
    
    GLabel_84=tk.Label(root1)
    GLabel_84["bg"] = "#ff3d00"
    GLabel_84["font"] = ft
    GLabel_84["fg"] = fg
    GLabel_84["justify"] = jf
    GLabel_84["text"] = "PassManager"
    GLabel_84["relief"] = "raised"
    GLabel_84.place(x=0,y=0,width=834,height=42)
    
    GLabel_780=tk.Label(root1)
    GLabel_780["bg"] = bg
    GLabel_780["font"] = ft
    GLabel_780["fg"] = fg
    GLabel_780["justify"] = jf
    GLabel_780["text"] = "WEBSITE:"
    GLabel_780.place(x=0,y=60,width=417,height=42)
    
    GLineEdit_185=tk.Entry(root1)
    GLineEdit_185["bg"] = bg
    GLineEdit_185["borderwidth"] = "3px"
    GLineEdit_185["font"] = ft        
    GLineEdit_185["fg"] = fg
    GLineEdit_185["justify"] = jf        
    GLineEdit_185.place(x=417,y=60,width=417,height=42)
    
    GLabel_207=tk.Label(root1)
    GLabel_207["bg"] = bg
    GLabel_207["font"] = ft
    GLabel_207["fg"] = fg        
    GLabel_207["justify"] = jf
    GLabel_207["text"] = "USERNAME:"
    GLabel_207.place(x=0,y=120,width=417,height=42)
    
    GLineEdit_800=tk.Entry(root1)
    GLineEdit_800["bg"] = bg        
    GLineEdit_800["borderwidth"] = "3px"
    GLineEdit_800["font"] = ft
    GLineEdit_800["fg"] = fg
    GLineEdit_800["justify"] = jf        
    GLineEdit_800.place(x=417,y=120,width=417,height=42)
    
    GLabel_724=tk.Label(root1)
    GLabel_724["bg"] = bg
    GLabel_724["font"] = ft
    GLabel_724["fg"] = fg
    GLabel_724["justify"] = jf
    GLabel_724["text"] = "PASSWORD:"
    GLabel_724.place(x=0,y=180,width=417,height=42)
    
    GLineEdit_708=tk.Entry(root1)
    GLineEdit_708["bg"] = bg
    GLineEdit_708["borderwidth"] = "3px"
    GLineEdit_708["font"] = ft        
    GLineEdit_708["fg"] = fg
    GLineEdit_708["justify"] = jf
    GLineEdit_708.place(x=417,y=180,width=417,height=42)
    
    GButton_429=tk.Button(root1)    
    GButton_429["bg"] = bg
    GButton_429["font"] = ft2    
    GButton_429["fg"] = fg
    GButton_429["justify"] = jf    
    GButton_429["text"] = "Send Data"
    GButton_429["relief"] = rf
    GButton_429.place(x=0,y=240,width=417,height=42)        
    GButton_429["command"] = GButton_429_command
        
    GButton_996=tk.Button(root1)
    GButton_996["bg"] = bg        
    GButton_996["font"] = ft2
    GButton_996["fg"] = fg
    GButton_996["justify"] = jf
    GButton_996["text"] = "Cancel"
    GButton_996["relief"] = rf        
    GButton_996.place(x=417,y=240,width=417,height=42)
    GButton_996["command"] = GButton_996_command
    
    GButton_452=tk.Button(root1)
    GButton_452["bg"] = bg
    GButton_452["font"] = ft2
    GButton_452["fg"] = fg
    GButton_452["justify"] = jf
    GButton_452["text"] = "See Data"
    GButton_452["relief"] = rf        
    GButton_452.place(x=0,y=300,width=417,height=42)
    GButton_452["command"] = GButton_452_command
    
    GButton_668=tk.Button(root1)
    GButton_668["bg"] = bg    
    GButton_668["font"] = ft2
    GButton_668["fg"] = fg
    GButton_668["justify"] = jf
    GButton_668["text"] = "Generate Password"        
    GButton_668["relief"] = rf
    GButton_668.place(x=417,y=300,width=417,height=42)
    GButton_668["command"] = GButton_668_command

    root1.mainloop()


    




def __init__2():
    global ft
    global ft2
    global GLineEdit_681
    global root2
    #setting title
    root2=tk.Tk()
    root2.title("undefined")
    root2.attributes('-alpha',0.9)
    root2["background"] = bg
    #setting window size
    width=834
    height=220
    screenwidth = root2.winfo_screenwidth()
    screenheight = root2.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root2.geometry(alignstr)
    ft = tkFont.Font(family='Times',size=22)
    ft2 = tkFont.Font(family='Times',size=14)
    root2.resizable(width=False, height=False)

    GLabel_132=tk.Label(root2)
    GLabel_132["bg"] = "#ff3d00"
    GLabel_132["font"] = ft
    GLabel_132["fg"] = fg
    GLabel_132["justify"] = jf
    GLabel_132["text"] = "Stored Data"
    GLabel_132["relief"] = "raised"
    GLabel_132.place(x=0,y=0,width=834,height=42)

    GLabel_216=tk.Label(root2)
    GLabel_216["bg"] = bg
    GLabel_216["font"] = ft
    GLabel_216["fg"] = fg
    GLabel_216["justify"] = jf
    GLabel_216["text"] = "Website"
    GLabel_216.place(x=0,y=60,width=417,height=42)

    GLineEdit_681=tk.Entry(root2)
    GLineEdit_681["bg"] = bg
    GLineEdit_681["borderwidth"] = "5px"
    GLineEdit_681["font"] = ft
    GLineEdit_681["fg"] = fg
    GLineEdit_681["justify"] = jf
    GLineEdit_681["text"] = "Entry"
    GLineEdit_681.place(x=417,y=60,width=417,height=42)

    GButton_199=tk.Button(root2)
    GButton_199["bg"] = bg
    GButton_199["font"] = ft2
    GButton_199["fg"] = fg
    GButton_199["justify"] = jf
    GButton_199["text"] = "Proceed"
    GButton_199["relief"] = rf
    GButton_199.place(x=0,y=120,width=417,height=42)
    GButton_199["command"] = GButton_199_command

    GButton_53=tk.Button(root2)
    GButton_53["bg"] = bg
    GButton_53["font"] = ft2
    GButton_53["fg"] = fg
    GButton_53["justify"] = jf
    GButton_53["text"] = "Cancel"
    GButton_53["relief"] = rf
    GButton_53.place(x=417,y=120,width=417,height=42)
    GButton_53["command"] = GButton_53_command

    GButton_117=tk.Button(root2)
    GButton_117["bg"] = bg
    GButton_117["font"] = ft2
    GButton_117["fg"] = fg
    GButton_117["justify"] = jf
    GButton_117["text"] = "See All"
    GButton_117["relief"] = rf
    GButton_117.place(x=0,y=180,width=834,height=42)
    GButton_117["command"] = GButton_117_command

    root2.mainloop()

def GButton_199_command():
    wd=encode('1',(GLineEdit_681.get()))
    cursor.execute('select website from passwords')
    websites=[]
    for i in cursor:
        websites.append(i[0])
    if wd in websites:
        see=cursor.execute('select * from passwords where website=%a'%wd)
        data=cursor.fetchall()
        for i in data:
            print('Username | Password')
            print(decode('1',i[1]),'|',decode('1',i[2]))
    else :
        print(GLineEdit_681.get(),'is not there')
    root2.destroy()


def GButton_53_command():
        root2.destroy()


def GButton_117_command():
    cursor.execute('select * from passwords')
    data=[]
    d=cursor.fetchall()
    print('Website | Username | Password')
    for i in d:
        print(decode('1',i[0]),'|',decode('1',i[1]),'|',decode('1',i[2]))
    root2.destroy()


def GButton_429_command():
    cursor.execute("INSERT INTO passwords VALUE('%s','%s','%s')"%(encode('1',GLineEdit_185.get()),encode('1',GLineEdit_800.get()),encode('1',GLineEdit_708.get())))
    cnx.commit()
    print('Data Updated')


def GButton_996_command():
    sys.exit()


def GButton_452_command():
    print('Fetching Data Please Wait')
    for i in range(10):
        print('.',end='')
        time.sleep(0.01)
    print()
    __init__2()


def GButton_668_command():
    __init__3()

__init__1()














