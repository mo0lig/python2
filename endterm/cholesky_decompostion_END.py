import math
def is_symmetric(matrix):
    # Check if the matrix is equal to its transpose
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix[0])))

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

def is_positive_definite(matrix):
    # Check if the matrix is symmetric
    if not is_symmetric(matrix):
        return False

    n = len(matrix)

    # Check if all leading principal minors have positive determinants
    for k in range(1, n + 1):
        submatrix = [row[:k] for row in matrix[:k]]
        determinant = dt(submatrix)
        if determinant <= 0:
            return False
    return True

def cholesky_decomposition(matrix):
    if is_symmetric(matrix) and is_positive_definite((matrix)):
        n = len(matrix)
        L = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    # Diagonal elements calculation
                    temp_sum = sum(L[i][k] ** 2 for k in range(j))
                    L[i][j] = (matrix[i][j] - temp_sum) ** 0.5
                else:
                    # Off-diagonal elements calculation
                    temp_sum = sum(L[i][k] * L[j][k] for k in range(j))
                    L[i][j] = (matrix[i][j] - temp_sum) / L[j][j]
        return L
    else:
        return("Matrix is not symmetric")


# Example usage:
matrix=[[4, 12, -16], [12, 37, -43], [-16, -43, 98]]

cholesky_result = cholesky_decomposition(matrix)

# Print the result
for row in cholesky_result:
    print(row)
