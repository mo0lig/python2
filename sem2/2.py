x=input("Enter the degree of converting in this format(10C or 100F):")
n=int(x[:-1])
if "C" in x:
    print((9 * n) / 5 + 32, "F")
if "F" in x:
    print((n - 32) * 5 / 9, "C")