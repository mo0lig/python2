def len(n):
    a=True
    b=1
    while a:
        while n>9:n=n*0.1
        b+=1
        if n<9:
            a=False
        return b
def summ(n):
    return n

n=int(input())
len=len(n)
print(summ(n))

