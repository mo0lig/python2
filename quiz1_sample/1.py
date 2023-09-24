s=input().split()
b=""
c=0
d=False
vow=["a","e","i","o","u"]
list=[]
ll=[]
for k in s:
    for i in k:
        i.islower()
        list.append(i)
        for i in range(len(list)):
            if i==0 and list[i]in vow:
                print(k+"yay")
                break
            else:
                d=True
            if list[i] in vow:
                break
            else:
                b+=list[i]
                c+=1
    ll.append(c)
for i in ll:
    if d is True:
        print(i[c::]+b+"ay")