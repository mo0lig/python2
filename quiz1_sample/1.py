vow=["a","e","i","o","u","A","E","I","O","U"]
s=input().split()
for i in s:
    if i[0] in vow:
        print(i+"yay")
    elif i.isalpha():
        print(i[1:]+i[:1]+"ay",end=" ")
