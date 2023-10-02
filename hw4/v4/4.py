n=int(input())
a,b,c=0,0,0
sum=0
f=[]
list=[]
for i in range(n):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    sum=(a+b)*c
    list.append(sum)
print(list)
