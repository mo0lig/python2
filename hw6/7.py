import math
import re
def valid(num):
    s=num
    x=s.split("-")
    for i in x:
        if len(i)!=4:
            return False
    num=re.sub("-","",num)
    if num.isnumeric():
        if len(num)==16:
            if re.match("^[456]\d{15}$",num) and not re.search("(\d)\1{3,}",num):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def check(n):
    dict={}
    for i in range(n):
        x=input()
        k=dict.keys()
        if valid(x):
            dict[x]="Valid"
        else:
            dict[x]="Invalid"
    return dict

n=int(input())
print(check(n))