import re
def email(n):
    list=[]
    for i in range(n):
        x=input()
        if re.search("@",x):
            list.append(x)
    return sorted(list)
n=int(input())
print(email(n))