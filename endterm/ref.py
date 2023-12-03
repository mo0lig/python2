def swap(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale(matrix, row, scalar):
    matrix[row] = [scalar * element for element in matrix[row]]

def add_row(matrix, i, j, scalar):
    for k in range(len(matrix[0])):
        matrix[j][k] = matrix[j][k] + scalar * matrix[i][k]

def ref(matrix):
    row, column,numc = len(matrix), len(matrix[0]),0
    for numr in range(row):
        while numc < column and matrix[numr][numc] == 0:   
            numc += 1
        if numc == column:
            continue   
        scale(matrix, numr, 1 / matrix[numr][numc])
        for i in range(numr + 1, row):
            add_row(matrix, numr, i, -matrix[i][numc])
        numc += 1
    return matrix
                
n=int(input("nxm size of matrix:"))
m=int(input("nxm size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(m):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]    

rmatrix = ref(matrix)
print("Row Echelon Form:")
print(rmatrix)
