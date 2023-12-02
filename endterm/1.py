def print_matrix(matrix):
    for row in matrix:
        print(row)

def swap_rows(matrix, i, j):

    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale_row(matrix, row, scalar):

    matrix[row] = [scalar * element for element in matrix[row]]

def add_scaled_row(matrix, source_row, destination_row, scalar):
  
    matrix[destination_row] = [matrix[destination_row][i] + scalar * matrix[source_row][i]
                               for i in range(len(matrix[0]))]

def row_echelon_form(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    pivot_col = 0  
    
    for pivot_row in range(num_rows):
       
        while pivot_col < num_cols and matrix[pivot_row][pivot_col] == 0:
            pivot_col += 1
        
        if pivot_col == num_cols:
          
            continue
        
       
        scale_row(matrix, pivot_row, 1 / matrix[pivot_row][pivot_col])
        
      
        for row in range(pivot_row + 1, num_rows):
            add_scaled_row(matrix, pivot_row, row, -matrix[row][pivot_col])
       
        pivot_col += 1

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

ref_matrix = row_echelon_form(matrix)
print("Row Echelon Form:")
print_matrix(ref_matrix)
