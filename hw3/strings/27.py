s=input().split()
list=[]
a=''
for i in s:
    for j in range(len(i)):
        a+=i[len(i)-j-1]
    list.append(a)
    a=''
for i in list:
    print(i,end=' ')


