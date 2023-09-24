s=input().split(',')
list=[]
c=""
x,y,a,b='','','',''
for i in s:
    for j in i:
        if j=="'":
            continue
        else: c+=j
    list.append(c)
    c=""
a,b=list[0],list[1]
x=b[:1]+a[1:]
y=a[:1]+b[1:]
print(x,y)
        
