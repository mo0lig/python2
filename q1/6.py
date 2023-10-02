def func(a, b, c):
    aa=a*a
    bb=b*b
    cc=c*c
    smax = max(aa,bb,cc)

    if smax==aa+bb:
        return "R"
    elif smax<aa+bb:
        return "A"  
    else:
        return "O" 

n=int(input())
list=[]
a,b,c=0,0,0
for i in range(n):
    s=input().split()
    a=int(s[0])
    b=int(s[1])
    c=int(s[2])
    result = func(a,b,c)
    list.append(result)   
    
for i in list:
    print(i,end=" ")
