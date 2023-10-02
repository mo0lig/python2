n=int(input())
list=[]
li=[]
for i in range(n):
    s=[int(x) for x in input().split()]   
    x=(s[1]-s[3])/(s[0]-s[2])
    y=s[1]-s[0]*x
    list.append(x)
    list.append(y)     
    li.append(list) 
    list=[]    
print(li)
