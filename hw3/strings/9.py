s=input()
x=int(input())
a=""
try:
    if len(s)<0 or x<0:
        raise Exception()
except:
    print("Enter letter or index in correct form")
else:
    for i in range(len(s)):
        if x-1==i:
            continue
        else:
            a+=s[i]
finally:
    print(a)