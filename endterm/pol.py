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
def coef(matrix):
    return [[((-1)**(i + j))*dt(minor(matrix,i,j)) for j in range(len(matrix[i]))] for i in range(len(matrix))]
def polynom(matrix):
    sum=0
    det=dt(matrix)
    for i in range(n):
        for j in range(n):
            if i==j:
                sum+=matrix[i][j]
    if n==2:
        if det<0:
            if sum>0:
                return (f"t^2 - {sum}t - {abs(dt(matrix))}")
            else:
                return (f"t^2 + {abs(sum)}t - {abs(dt(matrix))}")
        elif det>0:
            if sum>0:
                return (f"t^2 - {sum}t + {dt(matrix)}")
            else:
                return (f"t^2 + {sum}t + {dt(matrix)}")
    if n==3:
        cf=dt(coef(matrix))
        if det<0:
            if sum>0:
                if cf>0:
                    return f"t^3 - {sum}t^2 + {cf}t + {abs(dt(matrix))}"
                else:
                    return f"t^3 - {sum}t^2 - {abs(cf)}t + {abs(dt(matrix))}"   
            else:
                if cf>0:
                    return f"t^3 + {abs(sum)}t^2 + {cf}t + {abs(dt(matrix))}"
                else:
                    return f"t^3 + {abs(sum)}t^2 - {abs(cf)}t + {abs(dt(matrix))}" 
        elif det>0:
            if sum>0:
                if cf>0:
                    return f"t^3 - {sum}t^2 + {cf}t - {dt(matrix)}"
                else:
                    return f"t^3 - {sum}t^2 - {abs(cf)}t - {dt(matrix)}"
            else:
                if cf>0:
                    return f"t^3 + {abs(sum)}t^2 + {cf}t - {dt(matrix)}"
                else:
                    return f"t^3 + {abs(sum)}t^2 - {abs(cf)}t - {dt(matrix)}"
        
          
n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
print(polynom(matrix))
