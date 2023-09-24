s=input()
a,b="",""
for i in range(len(s)):
    a,b=s[0],s[len(s)-1]
print(b+s[1:len(s)-1]+a)