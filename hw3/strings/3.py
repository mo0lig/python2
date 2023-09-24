s=input()
try:
    if len(s)<3:
        if (type(s) is not str) or (len(s) == 1):
            raise Exception()
except:
    print()
else:
    print(s[0:2]+s[-2:])