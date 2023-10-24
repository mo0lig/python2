import tkinter as tk
import re
global db
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def database(fil):
    db = {}
    with open(fil, 'r') as file:
        for line in file:
            each=line.split(",")
            db[each[0]] = each[1]
    return db



def data_to_database(db, fil):
    with open(fil, 'w') as file:
        for name, pas in db.items():
            file.write(f"{name},{pas}\n")

fil='C:\\Users\\Админ\\OneDrive\\Документы\\python2\\python2\\sem7\\database.txt'
logins = database(fil)

def show_db():
    print(database(fil))
def add_user():
    name=input("Enter your login please:")
    while name in logins:
        name=input("Another name:")
    pas=input("password:")
    while  not check_pas(pas):
        pas=input("Another password:")
    logins[name]=pas
    print("Add user command is done")
    data_to_database(logins,fil)
    
          
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
            
def change_pas():
    name=input("PLease,enter your login:")
    while name not in logins:
        name=input("Another name:")
    oldpas=input("Input password:")
    if logins[name]==oldpas:
        newpas=input("New password:")
        while  not check_pas(newpas):
            newpas=input("Another password:")
        logins[name]=newpas
        data_to_database(logins, fil)
    else:
        print("your password is not correct")
def main():
    wind=tk.Tk()
    wind.title("Main")
    wind.configure(bg=_from_rgb((255, 229, 204)))
    wind.geometry("1000x500")
    mess=tk.Label(wind,text="Welcome",fg=_from_rgb((0, 0, 255)),bg=_from_rgb((255, 229, 204))).place(x=500,y=0)
    lab1=tk.Label(wind,text="Please, choose one of the actions",fg=_from_rgb((0, 0, 255)),bg=_from_rgb((255, 229, 204))).place(x=0,y=50)
    act1=tk.Button(wind,text="Show Database",command=show).place(x=20,y=70)
    act2=tk.Button(wind,text="Register",command=reg).place(x=20,y=100)
    act3=tk.Button(wind,text="Change password",command=change).place(x=20,y=130)
    act4=tk.Button(wind,text="Exit", command=quit).place(x=20,y=160) 
    wind.mainloop()
def show():
    show=tk.Tk()
    show.configure(bg=_from_rgb((255, 229, 204)))
    show.geometry("1000x500")
    mess=tk.Label(show,text="Data:",fg=_from_rgb((0, 0, 255)),bg=_from_rgb((255, 229, 204))).place(x=500,y=0) 
    show.mainloop()
"""def add_user(usern,userp):
    mess=tk.Lable()
    while usern in logins:
        
    pas=input("password:")
    while  not check_pas(pas):
        pas=input("Another password:")
    logins[name]=pas
    print("Add user command is done")
    data_to_database(logins,fil)"""
def reg():
    reg=tk.Tk()
    reg.configure(bg=_from_rgb((255, 229, 204)))
    reg.geometry("1000x500")
    user_name = tk.Label(reg, text = "Username").place(x = 40,y = 60)          
    user_password = tk.Label(reg, text = "Password").place(x = 40,y = 100)  
    submit_button = tk.Button(reg, text = "Submit",command=(lambda:usern.get(),userp.get())).place(x = 40,y = 130)
    usern = tk.Entry(reg,width = 30).place(x = 110,y = 60)  
    userp = tk.Entry(reg,width = 30).place(x = 110,y = 100) 
    reg.grid(x=0,y=1)
    reg.mainloop()
def change():
    change=tk.Tk()
    change.configure(bg=_from_rgb((255, 229, 204)))
    change.geometry("1000x500")
    user_name = tk.Label(change, text = "Username").place(x = 40,y = 60)          
    user_password = tk.Label(change, text = "Password").place(x = 40,y = 100)  
    new_pass = tk.Label(change, text = "Newpass").place(x = 40,y = 130)
    new_area = tk.Entry(change,width = 30).place(x = 110,y = 130)
    submit_button = tk.Button(change, text = "Submit").place(x = 40,y = 160)
    user_name_input_area = tk.Entry(change,width = 30).place(x = 110,y = 60)  
    user_password_entry_area = tk.Entry(change,width = 30).place(x = 110,y = 100) 
    exit = tk.Button(change, text = "Exit",command=quit).place(x = 120,y = 160)
    return change
    change.grid(x=0,y=1)
    change.mainloop()
    

main()
