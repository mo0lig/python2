n=int(input())
lis=[]
dic={}
a=True
for i in range(n):
    x=int(input())
    lis.append(x)
    
for i in lis:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1

for i in dic:
    if dic[i]>1:
        print("No")
        a=False
        break
if a==True:
    print("Yes")
        