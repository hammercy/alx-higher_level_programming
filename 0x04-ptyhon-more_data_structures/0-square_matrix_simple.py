def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len(matrix[0])
    mat_sqr = [[0 for i in range(col)] for j in range(row)]
    for r in range(row):
        for c in range(col):
            mat_sqr[r][c] = matrix[r][c]**2
    return mat_sqr
