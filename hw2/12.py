med=0
a=int(input("Input first number: "))
b=int(input("Input second number: "))
c=int(input("Input third number: "))
if a>b:
    if a<c:
        med=a
    elif b>c:
        med=b
    else:
        med=c
else:
    if a>c:
        med=a
    elif b<c:
        med=b
    else:
        med=c
print("The median is",med)