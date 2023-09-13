import random
n=random.randint(1,9)
print(n)
x=int(input("Please, enter your number:"))
while x!=n :
    if n>x:
        print("Your number is smaller than our numer")
        x=int(input("Please, enter your number:"))
    elif n<x:
        print("Your number is bigger than our number")
        x=int(input("Please, enter your number:"))
else:
    print("Well guessed")

        
