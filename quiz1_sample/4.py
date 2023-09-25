a=int(0)
m=''
lis=[]
dic={}
n=int(input())
for i in range(n):
    x=input()
    lis.append(x)

for i in lis:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
        
for i in dic:
    if dic[i]>a:
        a=dic[i]
        m=i
print(m)