list=[]
l=[]
n=int(input())
for i in range(n):
    x=int(input())
    list.append(x)
    if i==0:
        l.append(x)
    if i==n-1:
        l.append(x)
print(l)
