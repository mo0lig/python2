n=int(input())
x="*"
s=0
for i in range(1,n+1):
    print(x*i)
for i in range(1,n):
    s=n-i
    print(x*s)