def lu_decomposition(matrix):
    n = len(matrix)

    # Initialize L as an identity matrix and U as a zero-filled matrix
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Upper triangular matrix
        for k in range(i, n):
            sum_ = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matrix[i][k] - sum_

        # Lower triangular matrix
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0  # Diagonal elements of L are 1
            else:
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (matrix[k][i] - sum_) / U[i][i]

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
