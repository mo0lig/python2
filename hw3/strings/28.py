dic={}
s=input()
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    k=dic.keys()
    print(i, dic[i])
