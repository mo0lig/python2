def rectangle(n,m):
    for i in range(m):
        for j in range(n):
            print("*",end="")
        print()
n=int(input("n:"))
m=int(input("m:"))
rectangle(n,m)