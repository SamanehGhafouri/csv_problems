def matrix_transpose(matrix):
    transpose = []
    for _ in range(len(matrix[0])):
        li = [0 for _ in range(len(matrix))]
        transpose.append(li)
    # print(transpose)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            transpose[col][row] = matrix[row][col]
    return transpose


matrix_m = [[1, 2, 3], [4, 5, 6]]
transpose = matrix_transpose(matrix_m)
print(transpose)
