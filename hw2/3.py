a=int(input("Input a dog's age in human years:"))
b=0
if a<=2:
    b=a*10.5
else:
    a-=2
    b=21+a*4
print("The dog's age in dog's years is", b)