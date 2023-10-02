L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
s =input()
dd=True
for i in L:
    if len(i)==len(s):
        for j in range(len(s)):
            if  s[j]!="*" and i[j]!=s[j]:
                dd=False
                break
        if dd:
            print(i,end=" ")