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

def get_sol(matrix,sol):
    l=list()
    for i in range(len(matrix)):
        A = []
        for j in range(n):  
            current= matrix[j]
            modified= []
            for index in range(len(current)):
                if index < i:
                    modified.append(current[index])
                elif index == i:
                    modified.append(sol[j])
                else:
                    modified.append(current[index])
            A.append(modified)
        l.append(dt(A)/dt(matrix))
    for i in range(len(l)):
        print(f"x{i}={l[i]}")
        
n=int(input("nxm size of matrix:"))
m=int(input("nxm size of matrix:"))
matrix=list()
ll=[]
sol=list()
for i in range(n):
    for j in range(m):
        x=int(input(f"[{i}][{j}]="))
        if j==m-1:
            sol.append(x)
        else:
            ll.append(x)
    matrix.append(ll)
    ll=[]
get_sol(matrix,sol)

