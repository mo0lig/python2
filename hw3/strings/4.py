dic={}
s=input()
a=""
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
    if dic[i]>1:
        a=a+"$"
    else:
        a=a+i
print(a)