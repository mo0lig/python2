from sympy import Symbol 
from sympy import * 
def minor(matrix,i,j):
    mat=list()
    lis=[]
    for k in range(len(matrix)):
        if k==i:
            continue
        else:
            for s in range(len(matrix)):
                if s==j:
                    continue
                else:
                    lis.append(matrix[k][s])
            mat.append(lis)
            lis=[]
    return mat
                
def dt(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    if len(matrix)==2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det=0
    for k in range(len(matrix)):
        det += (matrix[0][k] * (-1)**k) * dt(minor(matrix,0,k))
    return det

def multiply(matrix,coef):
    return [[element * coef for element in row] for row in matrix] 

def substract(A, B):
    try:
        row = len(A[0])
    except TypeError:
        for i in range(len(A)):
            A[i] -= B[i]
    else:
        for i in range(len(A)):
            for j in range(row):
                A[i][j] -= B[i][j]
    return A

n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
identity=list()
for i in range(n):
    for j in range(n):
        if i==j:
            ll.append(1)
        else:
            ll.append(0)
    identity.append(ll)
    ll=[]
    
t=Symbol("x")

iden=multiply(identity, t)
    
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
    
matrix=substract(matrix,iden)
result=(-1)**n * dt(matrix)
print(result)

