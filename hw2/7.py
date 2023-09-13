s=input()
a=False
for i in s:
    if i.isnumeric():
        print("The string is an integer")
        a=True
        break
    else:
        continue
if a==False:
    print("The string is not an integer")