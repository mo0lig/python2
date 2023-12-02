def swap(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale(matrix, row, scalar):
    matrix[row] = [scalar * element for element in matrix[row]]

def add_row(matrix, sr, dr, scalar):
    matrix[dr] = [matrix[dr][i] + scalar * matrix[sr][i] for i in range(len(matrix[0]))]

def ref(matrix):
    nr, nc = len(matrix), len(matrix[0])
    pc = 0  
    
    for pr in range(nr):
       
        while pc < nc and matrix[pr][pc] == 0:
            pc += 1
        
        if pc == nc:
          
            continue
        
       
        scale(matrix, pr, 1 / matrix[pr][pc])
        
      
        for row in range(pr + 1, nr):
            add_row(matrix, pr, row, -matrix[row][pc])
       
        pc += 1

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

rmatrix = ref(matrix)
print("Row Echelon Form:")
print(rmatrix)
