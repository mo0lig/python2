s=input().split()
dic={}
mm={}
max,smax=0,0
a=''
t=False
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in s:
    if dic[i]>max:
        max=dic[i]
    elif max==dic[i] and max!=1:
        t=True
        d=mm.keys()
        if dic[i] in d:
            mm[dic[i]]+=1
        else:
            mm[dic[i]]=1
    elif dic[i]>smax:
        smax=dic[i]
        a=i

if t==True:
    for i in dic:
        print(i,dic[i])
else:
    print(a,dic[a])


"""dic={}
s=input().split()
max,smax=0,0
x=''
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in s:
    if dic[i]>max:
        max=dic[i]
    elif dic[i]<max and dic[i]>smax:
        smax=dic[i]
        x=i
print(i,smax)"""