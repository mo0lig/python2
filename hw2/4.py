s=input()
vow=["a","e","i","o","u"]
if s.isalpha():
    s.lower()
    if s in vow:
        print(s,"is vowel")
    else: print(s,"is consonant")