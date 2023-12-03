def matrix_vector_multiply(matrix, vector):
    result = []
    for row in matrix:
        result.append(sum(x * y for x, y in zip(row, vector)))
    return result

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def find_image_and_kernel(matrix):
    # Find the image (column space)
    image_basis = []
    for i in range(len(matrix[0])):
        basis_vector = [0] * len(matrix[0])
        basis_vector[i] = 1
        image_basis.append(matrix_vector_multiply(matrix, basis_vector))

    # Find the kernel (null space)
    augmented_matrix = [row + [0] for row in matrix]
    reduced_row_echelon_form(augmented_matrix)

    kernel_basis = []
    for row in augmented_matrix:
        kernel_vector = row[:len(row)-1]
        kernel_basis.append(kernel_vector)

    return image_basis, kernel_basis

def reduced_row_echelon_form(matrix):
    lead = 0
    rowCount = len(matrix)
    columnCount = len(matrix[0])

    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return

        matrix[i], matrix[r] = matrix[r], matrix[i]

        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]

        for i in range(rowCount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv*rv for rv, iv in zip(matrix[r], matrix[i])]

        lead += 1

# Example usage:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

image, kernel = find_image_and_kernel(matrix)

print("Matrix:")
for row in matrix:
    print(row)
print("\nImage (Column Space):")
for vector in image:
    print(vector)
print("\nKernel (Null Space):")
for vector in kernel:
    print(vector)
