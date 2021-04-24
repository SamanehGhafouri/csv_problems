def sort_elements_in_columns(matrix):

    transpose = [[0 for _ in line] for line in matrix]
    sorted_transpose = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            transpose[col][row] = matrix[row][col]

    for line in transpose:

        sorted_line = sorted(line)
        sorted_transpose.append(sorted_line)

    for row in range(len(sorted_transpose)):
        for col in range(len(sorted_transpose[0])):
            transpose[col][row] = sorted_transpose[row][col]
    return transpose


matrix_m = [[1, 9, 3], [5, 7, 3], [3, 10, 1]]
result = sort_elements_in_columns(matrix_m)
print(result)