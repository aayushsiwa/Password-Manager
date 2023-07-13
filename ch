import tkinter as tk
import mysql.connector as m
from mysql.connector import errorcode
import sys
import time
from ende import encode
from ende import decode
import os
import string
import random
import tkinter.ttk as ttk
fname='Details.txt'
# Function for calculation of password
def low():
    entry.delete(0, tk.END)
    pw.delete(0,tk.END)
    # Get the length of passowrd
    length = int(var.get())
    print(int(var.get()))
    digits =string.punctuation+string.digits+string.ascii_lowercase+string.ascii_lowercase
    password = ""
    for i in range(0,length):
        password+=random.choice(digits)
    return password
# Function for generation of password
def generate():
    a=low()
    entry.insert(10,a)
    pw.insert(10,a)

# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    root.clipboard_clear()
    root.clipboard_append(random_password)
def window21():
    global entry
    global root
    global var
    global bl3
    #Create GUI Window.....
    root = tk.Tk()
    # Title of GUI Window...
    root.title("Random Password Generator")
    # Create Label and Entry box
    Random_password = tk.Label(root,text="Password")
    Random_password.grid(row=0,sticky='nsew')
    entry = tk.Entry(root)
    entry.grid(row=0,column=1,sticky='nsew')
    #Create Label for Lenght of Password..
    c_label = tk.Label(root,text="Length")
    c_label.grid(row=1,sticky='nsew')
    #create Buttons ..
    copy_button = tk.Button(root,text="Copy",command=copy1)
    copy_button.grid(row=0,column=2,sticky='nsew')
    generate_button = tk.Button(root,text="Generate",command=generate)
    generate_button.grid(row=0,column=3,sticky='nsew')
    exit_button = tk.Button(root,text="Exit",command=root.quit)
    exit_button.grid(row=0,column=4,sticky='nsew')
    values=[8,9,10,11,12,13,14,15,16,17,18]
    var=tk.IntVar(root)
    var.set(8)
    menu=tk.OptionMenu(root,var,*values)
    menu.grid(row=1,column=1,sticky='nsew')
    #entr=tk.Entry(root)
    #entr.grid(row=1,column=1)
    bl3=[copy_button,generate_button,exit_button]
    tk.Grid.columnconfigure(root,0,weight=1)
    tk.Grid.columnconfigure(root,1,weight=1)
    tk.Grid.columnconfigure(root,2,weight=1)
    tk.Grid.columnconfigure(root,3,weight=1)
    tk.Grid.columnconfigure(root,4,weight=1)
    tk.Grid.rowconfigure(root,0,weight=1)
    root.mainloop()
def read(fname):
    global l
    f=open(fname,'r')
    l=f.readlines()

#read(fname)
#r=l[0]
try:
        cnx = m.connect(user='root',password='aayush')
        #print('Connected to MySql')
except m.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
#os.remove(fname)
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
cnx=m.connect(user='root',password='aayush',database=f'{DATABASE}')
cursor=cnx.cursor()
cursor.execute('SHOW TABLES')
tables=[]
for i in cursor:
    tables.append(i[0])
if 'passwords' not in tables:
    cursor.execute('create table passwords(website char(120) not null, username char(120) not null, password char(120) not null)')
def window():
    global ws
    global web
    global un
    global pw
    ws=tk.Tk()
    ws.title('Password Manager')
    ws.configure(bg='yellow')
    #ws.iconbitmap('second.ico')
    w=tk.Label(ws,text='Website: ',bg='yellow')
    w.config(font=('Courier','24','italic'))
    w.grid(row=1,sticky='nsew')
    web=tk.Entry(ws, font = ('Courier',24, 'italic'), width =10,  bd = 0.5, justify = 'left')
    web.grid(row=1,column=1,sticky='nsew')
    tk.Label(ws,text='',bg='yellow').grid(row=2,sticky='nsew')
    u=tk.Label(ws,text='Username: ',bg='yellow')
    u.config(font=('Courier','24','italic'))
    u.grid(row=3,sticky='nsew')
    un=tk.Entry(ws, font = ('Courier',24, 'italic'), width =10,  bd = 0.5, justify = 'left')
    un.grid(row=3,column=1,sticky='nsew')
    tk.Label(ws,text='',bg='yellow').grid(row=4,sticky='nsew')
    p=tk.Label(ws,text='Password: ',bg='yellow')
    p.config(font=('Courier','24','italic'))
    p.grid(row=5,sticky='nsew')
    pw=tk.Entry(ws, font = ('Courier',24, 'italic'), width =10,  bd = 0.5, justify = 'left')
    pw.grid(row=5,column=1,sticky='nsew')

    tk.Label(ws,text='',bg='yellow').grid(row=6,sticky='nsew')
def upd():
    cursor.execute("INSERT INTO passwords VALUE('%s','%s','%s')"%(encode('1',web.get()),encode('1',un.get()),encode('1',pw.get())))
    cnx.commit()
    print('Data Updated')
window()
def data():
    wd=encode('1',(websi.get()))
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
        print(websi.get(),'is not there')
def seeall():
    cursor.execute('select * from passwords')
    data=[]
    d=cursor.fetchall()
    print('Website | Username | Password')
    for i in d:
        print(decode('1',i[0]),'|',decode('1',i[1]),'|',decode('1',i[2]))

def see_data():
    global websi
    global bl2
    global w
    w=tk.Tk()
    w.title('DATA')
    w.geometry('500x500')
    w.configure(bg='yellow')
    webs=tk.Label(w, text = "WEBSITE: ",bg='yellow') #'password' is placed on position 10 (row - 1 and column - 0)
    webs.config(font=('Courier','24','italic'))
    webs.grid(row=1,sticky='nsew')
    websi=tk.Entry(w, font = ('Courier',24, 'italic'), width =10,  bd = 0.5, justify = 'left')
    websi.grid(row = 1, column = 1,sticky='nsew')
    tk.Label(w,text='',bg='yellow').grid(row =2,sticky='nsew')
    b5=tk.Button(w, text = 'ENTER', command =lambda: [data(),w.destroy()], font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='dark green',fg='white').grid(row=3,column=0,sticky='nsew')
    b6=tk.Button(w, text = 'CANCEL', command =lambda: [w.destroy()], font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='dark red',fg='white').grid(row=3,column=1,sticky='nsew')
    tk.Label(w,text='',bg='yellow').grid(row =4,sticky='nsew')
    b7=tk.Button(w, text= 'SEE ALL', command =lambda:[seeall()], font = ('Courier',24, 'italic'),  bd = 10,bg='white',fg='black').grid(row=5,column=0,columnspan=2,sticky='nsew')
    bl2=[b5,b6,b7]
    rn2=0
    tk.Grid.columnconfigure(w,0,weight=1)
    tk.Grid.columnconfigure(w,1,weight=1)
    for j in bl2:
        tk.Grid.rowconfigure(w,rn2,weight=1)
        rn2+=2
def fetch_data():
    print('Fetching Data Please Wait')
    for i in range(10):
        print('.',end='')
        time.sleep(0.01)
    print()
    see_data()

def window_2():
    global bl1
    b1=tk.Button(ws,text='SEND DATA',command=upd, font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='seagreen',fg='white').grid(row=7,column=0,sticky='nsew')
    tk.Label(ws,text='',bg='yellow').grid(row=8,sticky='nsew')
    b2=tk.Button(ws,text='CANCEL',command=ws.destroy, font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='dark red',fg='white').grid(row=7,column=1,sticky='nsew')
    b3=tk.Button(ws,text='SEE DATA',command=lambda:[fetch_data()], font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='blue',fg='white').grid(row=9,column=0,sticky='nsew')
    b4=tk.Button(ws,text='GENERATE \n PASSWORD',command=lambda:[window21()], font = ('Courier',24, 'italic'), width =10,  bd = 10,bg='dark red',fg='white').grid(row=9,column=1,sticky='nsew')
    bl1=[b1,b2,b3,b4]
    rn1=0
    for i in bl1:
        tk.Grid.rowconfigure(ws,rn1,weight=1)
        rn1+=2
    ws.mainloop()
tk.Grid.columnconfigure(ws,0,weight=1)
tk.Grid.columnconfigure(ws,1,weight=1)
window_2()
