def minor(matrix, i, j):
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

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def coef(matrix):
    return [[((-1)**(i + j))*dt(minor(matrix,i,j)) for j in range(len(matrix[i]))] for i in range(len(matrix))]

def multiply(matrix,coef):
    return [[element * coef for element in row] for row in matrix]

def inverse(matrix):
    if dt(matrix)==0:
        return ("Inverse does't exist.")
    return multiply(transpose(coef(matrix)), 1/dt(matrix))

n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
print(inverse(matrix))
