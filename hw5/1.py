import re
global db
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

fil='C:\\Users\\Админ\\OneDrive\\Документы\\python2\\python2\\hw5\\database.txt'
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


print("Welcome")        
action=int(input("Please, choose one of the options: 0-show database,1-add user,2-change password,3-exit:"))

if action==0:
    show_db()
elif action==1:
    add_user()
elif action==2:
    change_pas()

    