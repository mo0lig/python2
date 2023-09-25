a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list=[]
c=0
dic={}
for i in a:
    k=dic.keys()
    if i in k:
        dic[i]+=1
    else:
        dic[i]=1
for i in b:
    k=dic.keys()
    if i in k:
        dic[i]+=1
        list.append(i)
        
list.sort()
print(list)