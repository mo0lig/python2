import numpy as np
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
    
n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
if dt(matrix)==0:
    print("your matrix is singular")
else:
    print("Not singular")
