def lu_decomposition(matrix):
    n = len(matrix)
    
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    U = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0.0)
        U.append(row)

    for i in range(n):
        for k in range(i, n):
            U[i][k] = matrix[i][k] - sum(L[i][j] * U[j][k] for j in range(i))

        for k in range(i + 1, n):
            try:
                L[k][i] = (matrix[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
            except ZeroDivisionError:
                raise ValueError("Input matrix is singular.")

    return L, U

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    # Example usage
    A = [
        [4, 3, 2],
        [2, 1, 3],
        [3, 4, 1]
    ]

    L, U = lu_decomposition(A)

    print("Matrix A:")
    print_matrix(A)

    print("\nLower Triangular Matrix L:")
    print_matrix(L)

    print("\nUpper Triangular Matrix U:")
    print_matrix(U)
