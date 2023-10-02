s=[int(i) for i in input().split()]
a=True
for i in range(1,len(s)):
    if s[i-1]<=s[i]:
        continue
    else:
        print(i-1)
        a=False
        break

if a==True:
    print("[]")
