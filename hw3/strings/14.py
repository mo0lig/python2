s=input().split(",")
s.sort()
dic={}
for i in s:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    print(i,end=", ")

    