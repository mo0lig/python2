s=input()
x=''
for i in range(len(s)):
    if i%2==0:
        continue
    else:
        x+=s[i]
print(x)