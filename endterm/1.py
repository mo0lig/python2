import numpy as np
def minor(matrix,i,j,n):
    mat=list()
    lis=[]
    for k in range(n):
        if k==i:
            continue
        else:
            for s in range(n):
                if s==j:
                    continue
                else:
                    lis.append(matrix[k][s])
            mat.append(lis)
            lis=[]
    return mat
                
def det(mat):
    return (mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0])
def dt(matrix,n):
    if n==1:
        return matrix[0][0]
    if n==2:
        return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
    if n==3:
        return sum(matrix[0][k]*((-1)**k) * det(minor(matrix,0,k,n)) for k in range(n))
    
n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
print(dt(matrix,n))