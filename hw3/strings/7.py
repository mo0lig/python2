s=input()
a=s.find("not")
b=s.find("poor")

if a>0 and b>0 and a<b:
    print(s[:a]+"good" +s[b+4:len(s)])
else:
    print("Error")
    