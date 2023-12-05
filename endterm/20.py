from copy import *
def inner_product(v, w):
    return sum(v[i] * w[i] for i in range(len(v)))

def norm(v):
    return sum(x * x for x in v) ** 0.5
# def transpose(matrix):
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def transpose(matrix):
    mat = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        mat.append(row)
    return mat
def projection(v, w):
    dot_product = sum(v[i] * w[i] for i in range(len(v)))
    norm_squared = sum(x * x for x in w)
    return [dot_product / norm_squared * w[i] for i in range(len(w))]

def gram_schmidt(A):
    m, n = len(A), len(A[0])
    Q = [[0 for _ in range(n)] for _ in range(m)]
    R = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        v = [A[i][j] for i in range(m)]  # Extract the j-th column of A as a vector

        for i in range(j):
            R[i][j] = inner_product(Q[i], v)
            v = [v[k] - R[i][j] * Q[i][k] for k in range(m)]

        norm_v = norm(v)
        q = [v[k] / norm_v for k in range(m)]
        Q[j] = q
    D = [[inner_product(Q[i], transpose(A)[j]) for j in range(len(transpose(A)))] for i in range(len(Q))]
    for i in range(len(D)):
        for j in range(len(D[0])):
            if i>j:
                D[i][j]=0
                
    Q=transpose(Q)
    return Q, D

A=[[1,2,3],[0,1,4],[5,6,0]]
print(gram_schmidt(A))
