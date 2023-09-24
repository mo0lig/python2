s=input()
a=""
c=len(s)
if len(s)%4==0:
    for i in range(c):
        a+=s[c-i-1]
    print(a)
else:
    print("The length of your word is not multiple of 4")