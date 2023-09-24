s=input().split()
dic={}
max=0
a=''
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in s:
    if dic[i]>max:
        max=dic[i]
        a=i
    
print(a,max)