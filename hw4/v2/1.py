print("Welcome to Hangman!")
s=input()
l = ['_' for i in range(len(s))]
word = list(s)
while l != word:
    letter = input("Guess your letter:")
    if letter in word:
        for i in range(len(l)):
            if word[i] == letter:
                l[i] = letter
        for i in l:
            print(i, end="")
        print()
    else:
        print("Incorrect!")
print("Well done")