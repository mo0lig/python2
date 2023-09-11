n=int(input())
if (abs(1000 - n) <= 100):
    print("100 of 1000")
elif (abs(2000 - n) <= 100):
    print("100 of 2000")
else:
    print("none of them")
    print(False)