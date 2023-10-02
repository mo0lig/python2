n=int(input())
list=[]
dir={}
for i in range(n):
    k=dir.keys()
    x=int(input())
    dir[x]=i+1
    list.append(x)
list.sort()
for i in list:
    print(dir[i],end=" ")