s=input()
a=0
for i in range(len(s)):
    if i<4:
        if s[i].isupper():
            a+=1
if a>=2:
    print(s.upper())
else:
    print(s)