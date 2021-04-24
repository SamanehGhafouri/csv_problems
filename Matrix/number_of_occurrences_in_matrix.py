def number_of_occurrences(matrix):

    num_occurr_dict = {}

    for row in matrix:
        for col in row:

            if col in num_occurr_dict:
                num_occurr_dict[col] += 1
            else:
                num_occurr_dict[col] = 1

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):

            matrix[row_index][col_index] = num_occurr_dict[col]
    return matrix


matrix_m = [['A', 'B', 'C'], ['C', 'A', 'A'], ['F', 'G', 'B']]
result = number_of_occurrences(matrix_m)
print(result)