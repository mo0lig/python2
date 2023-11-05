from tkinter import *
from tkinter import messagebox
import pymysql
import re

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
wind = Tk()
wind.title('Login')
wind.geometry("450x270")

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

def login():
    n=name.get()
    pas=password.get()
    if name.get() == '':
        messagebox.showerror('Error','Enter your name')
    elif password.get() == '':
        messagebox.showerror('Error','Enter your password')
    else:
        db = pymysql.connect(
                    host="localhost",
                    port=3306,
                    user="root",
                    password='',
                    database="data",
                    cursorclass=pymysql.cursors.DictCursor)
        try:
            with db.cursor() as cursor: 
                check = "SELECT * FROM `users` WHERE `name`=%s AND `password`=%s"
                cursor.execute(check,(n,pas))
                dd = cursor.fetchone()
                if dd== None:
                    messagebox.showerror('Error','Incorrect email or password')
                    return
                else:
                    messagebox.showinfo('Success','correct')
                    wind.destroy()
                    import calculator
                db.commit()
        finally:
            db.close()
            name.delete(0,END)
            password.delete(0,END)

def open_reg():
    wind.destroy()
    import register
    
def change():
    wind.destroy()
    import change_pass

fram=Frame(wind,width=500,height=500,bg=_from_rgb((210, 226, 255)),bd=8).place(x=0,y=0)
#Getting data from entry
fname = StringVar()
passw = StringVar()

#Labels
lab1 = Label(fram,text="Login",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',20,'bold')).place(x=150,y=0)
nam = Label(fram,text="Name:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=50)
pas = Label(fram,text="Password:",fg="black",bg=_from_rgb((210, 226, 255)),font=('arial',15,'bold')).place(x=18,y=90)

#Entry
name = Entry(fram, width=30, borderwidth=1)
name.place(x=230,y=57)
password = Entry(fram, width=30, borderwidth=1)
password.place(x=230,y=97)

submit = Button(fram ,text="Login", width=8, borderwidth=5,height=2, font=('arial',10,'bold'), command=login).place(x=150,y=130)
reg = Button(fram ,text="Register", width=8, borderwidth=5,height=2, font=('arial',10,'bold'), command=open_reg).place(x=70,y=130)
pas = Button(fram ,text="Change pass", width=10, borderwidth=5,height=2, font=('arial',10,'bold'), command=change).place(x=230,y=130)

wind.mainloop()