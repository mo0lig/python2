def fword(words):
    smax= max(len(word) for word in words)
    lwords= [word for word in words if len(word) == smax]
    return lwords

with open("C:\\Users\\Админ\\OneDrive\\Документы\\python2\\dd.txt", "r") as file:
    content = file.read()
words = content.split()

lword= fword(words)
print("Longest word(s):", lword)
