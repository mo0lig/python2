def minor(m,i,j):
    mat=list()
    lis=[]
    for k in range(len(m)):
        if k==i:
            continue
        else:
            for s in range(len(m)):
                if s==j:
                    continue
                else:
                    lis.append(m[k][s])
            mat.append(lis)
            lis=[]
    return mat

def det(m):
    if len(m)==1:
        return m[0]
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*det(minor(m,0,c))
    return determinant
        
n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
print(getMatrixDeternminant(matrix))