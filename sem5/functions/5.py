n=int(input())
a=True
b=1
while a:
    n=n*0.1
    b+=1
    if n<9:
        a=False
print(b)
