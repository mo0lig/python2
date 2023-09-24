s=input()
a=""
for i in s:
    if i==".":
        i=","
    elif i==",":
        i="."
    a+=i
print(a)