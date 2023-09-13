n=int(input())
list=[]
e=0
o=0
for i in range(n):
    x=int(input())
    list.append(x)
for i in list:
    if i%2==0:
        e+=1
    else: o+=1
print("Number of even numbers :",e)
print("Number of odd numbers :", o)