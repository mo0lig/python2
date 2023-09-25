def f1(lis):
    l2=[]
    for i in lis:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2

def f2(lis):
    return list(set(lis))

n=int(input())
lis=[]
for i in range(n):
    x=int(input())
    lis.append(x)
    
print("List by loops:",f1(lis))
print("List by set:",f2(lis))