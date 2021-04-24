import unittest


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


class Test(unittest.TestCase):

    def test_number_of_occurrences(self):

        matrix = [['A', 'B', 'B', 'C'], ['B', 'C', 'A', 'C'], ['D', 'B', 'D', 'F']]
        actual = number_of_occurrences(matrix)
        expected = [[2, 4, 4, 3], [4, 3, 2, 3], [2, 4, 2, 1]]

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

    # matrix_m = [['A', 'B', 'C'], ['C', 'A', 'A'], ['F', 'G', 'B']]
    # result = number_of_occurrences(matrix_m)
    # print(result)
