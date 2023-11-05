from tkinter import *
from tkinter import messagebox
import pymysql
import re

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

wind = Tk()
wind.geometry("500x300")
wind.title("Change password")

def back():
    wind.destroy()
    import login

def check_pas(pas):
    counter = 0
    if re.findall("[0-9]", pas):
        counter+=1
    if re.findall("[a-z]", pas):
        counter+=1
    if re.findall("[A-Z]", pas):
        counter+=1
    if re.search("[@#$%^]", pas):
        counter += 1
    if len(pas)>7 and counter>=4:
        return True
    else:
        return False
    
def check_email(email):
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if re.match(pattern, email) is not None:
        return True
    else:
        return False
    
def submit():
    n=name.get()
    e=email.get()
    p1=password.get()
    p2=conpassword.get()
    
    if name.get() == '':
        messagebox.showerror('Error','Enter your name')
    elif email.get() == '':
        messagebox.showerror('Error','Enter your email')
    elif password.get() == '':
        messagebox.showerror('Error','Enter your password')
    elif conpassword.get() == '':
        messagebox.showerror('Error','Please, again enter your password')
    else:
        if p1==p2:
            messagebox.showerror('Error','Please,Enter another new password')
        elif check_pas(p2) and check_email(e):
            try:
                db = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password='',
                    database="data",
                    cursorclass=pymysql.cursors.DictCursor)
                print("Connected")
                try:
                    with db.cursor() as cursor: 
                        insert = "UPDATE `users` SET `password`=%s WHERE `name`=%s AND `email`=%s" 
                        cursor.execute(insert,(p2,n,e))
                        db.commit()
                        
                finally:
                    db.close()
                    name.delete(0,END)
                    email.delete(0,END)
                    password.delete(0,END)
                    conpassword.delete(0,END)
                    
            except Exception as ex:
                print("NOT")
                print(ex)
        else:
            if not check_pas(p2):
                messagebox.showerror('Error','Please, enter password in correct form')
            if not check_email(e):
                messagebox.showerror('Error','Please, enter email in correct form')

fram=Frame(wind,width=500,height=500,bg=_from_rgb((210, 226, 255)),bd=8).place(x=0,y=0)
#Getting data from entry
fname = StringVar()
emaail = StringVar()
passw = StringVar()
conpassw = StringVar()

#Labels
lab1 = Label(fram,text="Change password",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',20,'bold')).place(x=150,y=0)
nam = Label(fram,text="Name:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=50)
em = Label(fram,text="Email:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=90)
pas = Label(fram,text="Old Password:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=130)
pas1 = Label(fram,text="New Password:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=170)

#Entry
name = Entry(fram, width=30, borderwidth=1)
name.place(x=230,y=57)
email = Entry(fram, width=30, borderwidth=1)
email.place(x=230,y=97)
password = Entry(fram, width=30, borderwidth=1)
password.place(x=230,y=137)
conpassword = Entry(fram, width=30, borderwidth=1)
conpassword.place(x=230,y=177)

submit = Button(fram ,text="Change", width=16, borderwidth=5,height=2, font=('arial',12,'bold'), command=submit).place(x=150,y=210)
back = Button(fram, text="Login",width=8, borderwidth=5,height=2, font=('arial',12,'bold'),command=back).place(x=50,y=210)

wind.mainloop()