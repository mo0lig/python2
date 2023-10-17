import re
def valid(p):
    d=p
    s=p
    e=""
    if len(p)==16:
        s=s.split(" ")
        for i in s:
            e+=i
        if re.match("^+7\d{10}",e):
            return True
        else:
            return False  
    elif len(p)==11:
        if d.isnumeric():
            if re.match("^8\d{10}",d):
                return True
            else:
                return False
        else:
            return False
    elif len(p)==10:
        if re.match("^+\d{9}"):
            return True
        else:
            return False
    else:
        return False
    
def phone(n):
    for i in range(n):
        x=input()
        dict={}
        if valid(x):
            dict[x]="Valid"
        else:
            dict[x]="Invalid"
    return dict
    
    
    
n=int(input())
print(phone(n))