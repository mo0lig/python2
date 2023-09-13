password=input()
x=False
a,b,c=0,0,0
if 16>=len(password)>=6:
    x=True
    for i in password:
        if i.isnumeric():
            a+=1
        if i.isalpha():
            b+=1
        if i=="$" or i=="#" or i=="@":
            c+=1
if x==True and a>=1 and b>=1 and c>=1:
    print("Your password is valid")
else: print("Your password form is not correct")