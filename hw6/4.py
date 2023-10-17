
def text(n):
    list=[]
    l=[]
    for i in range(n):
        x=input()
        l.append(x)
        x=x.replace("&&||","")
        x=x.replace("&&","and")
        x=x.replace("||","or")
        list.append(x)
    return list

n=int(input())
print(text(n))