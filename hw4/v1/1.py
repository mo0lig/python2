n=int(input("Please,choose one of numbers 0 or 1, 0 if you want to encrypt, 1 if you want to decrypt string:"))
xx=''
if n==0:
    s=input("Please,enter the letter that you wnat to encrypt:")
    for i in range(len(s)):
        if i%2==0:
            xx+=s[i]
    for i in range(len(s)):
        if i%2!=0:
            xx+=s[i]
if n==1:
    s=input("Please,enter the letter that you wnat to decrypt:")
    c=(len(s)+1)//2
    first=s[:c]
    second=s[c:]
    if len(s)%2==0:
        for i in range (c):
            xx+=(first[i]+second[i])
    else:
        for i in range (1,c+1):
            start=i-1
            xx+=first[start:i]+second[start:i]
print(xx)

    
    