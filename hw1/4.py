l=input().split(",")
list=[]
for i in l:
    list.append(i)
t=tuple(list)
print("List:")
[print(x) for x in list]
print("tuple:")
[print(x) for x in t]

print(type(list))
print(type(t))