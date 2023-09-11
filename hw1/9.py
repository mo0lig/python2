l=input("Enter a values of list:")
p=False
l=l.split()
lii=[]
for i in l:
    lii.append(i)
x=input("Value:")
for i in lii:
    if x in i:
        p=True
print(p)