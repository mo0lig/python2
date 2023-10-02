print("Welcome to Hangman!")
s='EVAPORATE'
l=list(s)
a=False
while a!=True:
    x=input("Guess your letter:")
    if x not in l:
        print("incorrect")
    else:
        for i in range(len(l)):
            if x==l[i]:
                for j in range(len(l)):
                    if j==i:
                        print(l[i],end="")
                    else:
                        print("_",end="")
        
    
            
    