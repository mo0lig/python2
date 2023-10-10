def sum_digits(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
n=int(input())
sum_digits(n)