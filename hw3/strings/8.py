n=int(input())
list=[]
a,b=0,0
s=''
for i in range(n):
    x=input()
    list.append(x)
for i in list:
    a=len(i)
    if(b<a):
        b=a
        s=i
print(s,b)