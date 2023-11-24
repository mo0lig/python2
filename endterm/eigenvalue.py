import math

def eigenvals(A):
    n = len(A)
    eigenvalues = []
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                continue
        # Handle the case where the matrix is not invertible
        try:
            det = determinant(A[:i + 1])
            inv = invert(A[:i + 1], det)
            eigenvalues.append((det, inv))
        except ZeroDivisionError:
            pass
    return eigenvalues

def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        det = 0
        for i in range(n):
            det += A[i][0] * minor(A, i, 0)
        return det

def minor(A, i, j):
    n = len(A)
    temp = [[0] * (n - 1) for _ in range(n - 1)]
    for k in range(n):
        if k != i:
            temp[k - 1][j - 1] = A[k][j]
    return determinant(temp)

def invert(A, det):
    n = len(A)
    inv = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            inv[i][j] = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                inv[i][j] = 1 / A[i][j]
    return inv

def eigenvects(A, eigenvalues):
    n = len(A)
    eigenvectors = []
    for eigenvalue, eigenvector in eigenvalues:
        for i in range(n):
            for j in range(n):
                if A[i][j] == 0:
                    continue
        # Handle the case where the matrix is not invertible
        try:
            inv = invert(A, eigenvalue)
            eigenvectors.append(inv)
        except ZeroDivisionError:
            pass
    return eigenvectors

n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
eigenvalues, eigenvectors = eigenvals(matrix), eigenvects(matrix, eigenvals(matrix))
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
for eigenvector in eigenvectors:
    print(eigenvector)