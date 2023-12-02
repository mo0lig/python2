def matrix_multiply(A, B):
 
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result
def matrix_identity(size):

    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def matrix_subtract(A, B):

    rows, cols = len(A), len(A[0])

    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

    return result

def matrix_determinant(matrix):

    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for i in range(size):
        submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        determinant += ((-1) ** i) * matrix[0][i] * matrix_determinant(submatrix)

    return determinant

def matrix_pow(matrix, power):

    result = matrix_identity(len(matrix))
    for _ in range(power):
        result = matrix_multiply(result, matrix)

    return result

def characteristic_polynomial(matrix):
    size = len(matrix)

    lambda_identity = matrix_subtract(matrix, matrix_identity(size))

    char_poly = [1]
    for i in range(size):
        factor = matrix_subtract(matrix_identity(size), matrix_pow(lambda_identity, i + 1))
        char_poly = matrix_multiply(char_poly, factor)

    return char_poly[0]

matrix = [[1, 2], [3, 4]]  
char_poly = characteristic_polynomial(matrix)

print("Matrix:")
for row in matrix:
    print(row)
print("\nCharacteristic Polynomial Coefficients:")
print(char_poly)

