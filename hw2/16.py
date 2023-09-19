n=int(input())
i,a=1,1
if n==0 or n>9:
    print("Please enter numbers between 1-9")
else:
    print("1")
    while i!=n:
        p=a+10**i
        print(p*(i+1))
        i+=1
        a=p
        