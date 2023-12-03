import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol 

# def draw():
#     fig,ax=plt.subplots()
#     ax.set_xlim((-15,15)) # interval of x axis
#     ax.set_ylim((-50,50)) # interval of y axis
#     ax.grid() #setka
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     x = np.linspace(-50,50,100) 
#     ax.plot(x,x**3 +12*x - 12,label=r'$f(x)=\ x^3 +12*x -12$')
#     ax.legend(loc='best', fontsize=8)
#     plt.savefig('figure_with_legend.png')
#     plt.show()
    
def gx(coef, n, g):
    l=list()
    x=Symbol("x")
    y=Symbol("y")
    b=0
    for i in range(n+1):
        l.append(coef[i] * x**(n-i))
        b+=coef[i] * g**(n-i)
    for i in range(n+1):
        y+=l[i]
    return b

def roots(n):
    l=list()
    j=0
    a=True
    while a:
        a=int(input("initial point:"))#value of initial x coordinate
        b=int(input("final point:"))#value of final x coordinate
        s=True
        i=1 
        while s:
            if (gx(coef,n,a)>=0 and gx(coef,n,b)>=0) or (gx(coef,n,a)<0 and gx(coef,n,b)<0): #By this condition we can find out whether there roots in a given user interval
                print("a or b is not in correct interval")  
                break
            else:
                c=(a+b)/2
                if gx(coef,n,a)*gx(coef,n,c)<0:
                    b=c
                    if abs(c-a)<0.01 or c==a:
                        s=False
                        l.append(c)
                else:
                    a=c
                    if abs(c-b)<0.01 or c==b:
                        s=False
                        l.append(c)
                i+=1
        j+=1
        if j==n:
            a=False
    for i in range(n):
        print(f"Eigenvalue-{i+1}={l[i]}")

n=int(input("Enter n:"))
coef=list()
print("Please, enter coef of polynomials:")
for i in range(n+1):
    x = int(input(f"{i}:"))
    coef.append(x)
     
roots(n)
