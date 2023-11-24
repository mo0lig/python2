import numpy as np

def find_RREF(matrix):
    matrix = np.array(matrix)
    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])

    for r in range(rowCount):
        if lead >= columnCount:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        leadValue = matrix[r][lead]
        matrix[r] = matrix[r] / leadValue

        for i in range(rowCount):
            if i != r:
                matrix[i] = matrix[i] - matrix[r] * matrix[i][lead]
        lead += 1

    return matrix

n=int(input("nxn size of matrix:"))
matrix=list()
ll=[]
for i in range(n):
    for j in range(n):
        x=int(input(f"[{i}][{j}]="))
        ll.append(x)
    matrix.append(ll)
    ll=[]
print(find_RREF(matrix))