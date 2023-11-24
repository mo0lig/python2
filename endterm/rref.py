def print_matrix(matrix):
    for row in matrix:
        print(row)

def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale_row(matrix, row, scalar):
    matrix[row] = [scalar * entry for entry in matrix[row]]

def add_rows(matrix, source_row, destination_row, scale=1):
    scaled_row = [scale * entry for entry in matrix[source_row]]
    matrix[destination_row] = [a + b for a, b in zip(matrix[destination_row], scaled_row)]

def rref(matrix):
    nrows, ncols = len(matrix), len(matrix[0])

    pivot_row = 0
    for pivot_col in range(ncols):
        # Find the next pivot row
        non_zero_rows = [i for i in range(pivot_row, nrows) if matrix[i][pivot_col] != 0]
        if non_zero_rows:
            pivot_row = non_zero_rows[0]
        else:
            continue

        # Make the pivot element 1
        scale_row(matrix, pivot_row, 1 / matrix[pivot_row][pivot_col])

        # Eliminate other elements in the current column
        for i in range(nrows):
            if i != pivot_row and matrix[i][pivot_col] != 0:
                scale = -matrix[i][pivot_col]
                add_rows(matrix, pivot_row, i, scale)

        # Move to the next pivot row
        pivot_row += 1

    return matrix

# Example usage:
matrix = [[1, 2, -1, 1],
          [2, 4, 1, 2],
          [3, 6, 0, 3]]

rref_matrix = rref(matrix)

print("Reduced Row-Echelon Form:")
print_matrix(rref_matrix)
