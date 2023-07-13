
import random
import tkinter as tk
import tkinter.font as tkFont
import mysql.connector as m
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from ende import encode
f='aayush13402@gmail.com'
t='22052177@kiit.ac.in'
p='xjiesbgfrnypkmyb'
bg = "#ff5722"
fg = "#ffffff"
rf = "groove"
jf = "center"


def __init__0():
    global root
    global GLineEdit_291
    global GLineEdit_290
    global GLineEdit_292
    global ft
    global ft2
    root = tk.Tk()
    root.title("PasswordManager")
    root.attributes('-alpha',0.9)
    root["background"] = "#ff5722"
    width=834
    height=282
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    ft = tkFont.Font(family='Times',size=22)
    ft2 = tkFont.Font(family='Times',size=14)
    root.resizable(width=False, height=False)
    
    GLabel_492=tk.Label(root)
    GLabel_492.pack(expand=True,fill='both')
    GLabel_492["bg"] = "#ff3d00"
    GLabel_492["font"] = ft
    GLabel_492["fg"] = fg
    GLabel_492["justify"] = jf
    GLabel_492["text"] = "MySQL Login"
    GLabel_492["relief"] = "raised"
    GLabel_492.place(x=0,y=0,width=834,height=42)
    
    GLabel_318=tk.Label(root)
    GLabel_318["bg"] = bg
    GLabel_318["font"] = ft
    GLabel_318["fg"] = fg
    GLabel_318["justify"] = jf
    GLabel_318["text"] = "Username:"
    GLabel_318.place(x=0,y=60,width=380,height=42)

    GLineEdit_291=tk.Entry(root)
    GLineEdit_291["bg"] = bg
    GLineEdit_291["borderwidth"] = "5px"
    GLineEdit_291["font"] = ft
    GLineEdit_291["fg"] = fg
    GLineEdit_291["justify"] = jf
    GLineEdit_291.place(x=380,y=60,width=452,height=42)
    GLineEdit_291.insert(0,'root')

    GLabel_317=tk.Label(root)
    GLabel_317["bg"] = bg
    GLabel_317["font"] = ft
    GLabel_317["fg"] = fg
    GLabel_317["justify"] = jf
    GLabel_317["text"] = "Password:"
    GLabel_317.place(x=0,y=120,width=380,height=42)

    GLineEdit_290=tk.Entry(root)
    GLineEdit_290["bg"] = bg
    GLineEdit_290["borderwidth"] = "5px"
    GLineEdit_290["font"] = ft
    GLineEdit_290["fg"] = fg
    GLineEdit_290["justify"] = jf
    GLineEdit_290.place(x=380,y=120,width=452,height=42)

    GButton_937=tk.Button(root)
    GButton_937["bg"] = bg
    GButton_937["font"] = ft2
    GButton_937["fg"] = fg
    GButton_937["justify"] = jf
    GButton_937["text"] = "Send OTP"
    GButton_937["relief"] = rf
    GButton_937.place(x=0,y=180,width=380,height=42)
    GButton_937["command"] = Send_OTP

    GLineEdit_292=tk.Entry(root)
    GLineEdit_292["bg"] = bg
    GLineEdit_292["borderwidth"] = "5px"
    GLineEdit_292["font"] = ft
    GLineEdit_292["fg"] = fg
    GLineEdit_292["justify"] = jf
    GLineEdit_292.place(x=380,y=180,width=452,height=42)

    GButton_930=tk.Button(root)
    GButton_930["bg"] = bg
    GButton_930["font"] = ft2
    GButton_930["fg"] = fg
    GButton_930["justify"] = jf
    GButton_930["text"] = "Login"
    GButton_930["relief"] = rf
    GButton_930.place(x=0,y=240,width=417,height=42)
    GButton_930["command"] = GButton_930_command

    GButton_931=tk.Button(root)
    GButton_931["bg"] = bg
    GButton_931["font"] = ft2
    GButton_931["fg"] = fg
    GButton_931["justify"] = jf
    GButton_931["text"] = "Cancel"
    GButton_931["relief"] = rf
    GButton_931.place(x=417,y=240,width=417,height=42)
    GButton_931["command"] = sys.exit
    
    bind_keys()
    
    root.mainloop()
    
    
    

def Send_OTP():
        GLineEdit_292.delete(0,tk.END)
        global Ot
        ms=MIMEMultipart()
        ms['Subject']='Password Manager One Time Password'
        ms['To']=t
        ms['From']=f
        d=['0','1','2','3','4','5','6','7','8','9']
        Ot=''
        for i in range(6):
            Ot+=random.choice(d)
        msText=MIMEText('''<html>
        <b>%s</b><i> is your One Time Password</i><br>
        <div style="float:left; clear:both;padding:10px 5px 10px 10px">
        <img src="https://cdn.dribbble.com/users/180787/screenshots/2018413/password_checking.gif" border="1" draggable=”false” style="display:block;width:100px;height:100px" >
        </div>
        </html>'''%Ot,'html')
        ms.attach(msText)
        s=smtplib.SMTP_SSL('smtp.gmail.com',465)
        s.login(f,p)
        s.send_message(ms)
        root.geometry('834x342')
        GLabel_491=tk.Label(root)
        GLabel_491.pack(expand=True,fill='both')
        GLabel_491["bg"] = "#ff3d00"
        GLabel_491["font"] = ft
        GLabel_491["fg"] = fg
        GLabel_491["justify"] = jf
        GLabel_491["text"] = "OTP Sent"
        GLabel_491["relief"] = "raised"
        GLabel_491.place(x=0,y=300,width=834,height=42)

def write_details(f,content):
        fn=open(f,'w')
        fn.write(content)
        fn.close()

def imp():
        import XII2

def GButton_930_command():
        r=str(random.random())
        a=encode(r,GLineEdit_291.get())
        b=encode(r,GLineEdit_290.get())
        write_details('Details.txt',(r+'\n'+a+'\n'+b))
        m.connect(user=GLineEdit_291.get() , password=GLineEdit_290.get())
        print('------'+Ot)
        print(GLineEdit_292.get())
        if Ot==GLineEdit_292.get():
            print('OTP accepted\nWelcome to PassManager\nby Aayush Siwach')
            print('Connected to MySQL')
            root.destroy()
            imp()
        else:
            print('OTP provided is wrong please try again')


def bind_keys():
        root.bind('<Return>',lambda event : [GButton_930_command()])


__init__0()