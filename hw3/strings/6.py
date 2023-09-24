s=input()
a="ing"
try:
    if len(s)<3:
        raise Exception()
except:
    print("Length should more than 3")
else:
    if a in s:
        print(s+"ly")
    else:
        print(s+a)