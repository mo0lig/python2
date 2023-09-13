n=int(input())
m=int(input())
list=[]
ll=[]
for i in range(n):
    for j in range(m):
        ll.append(i*j)
    list.append(ll)
    ll=[]
print(list)