import csv
import random
from typing import List
import unittest
from pprint import pprint


def generate_numbers_in_csv_file(file_name, row, column, range_from, range_to):
    with open(file_name, 'w') as w_file:
        file_writer = csv.writer(w_file)

        for line in range(row):
            file_writer.writerow(random.randint(range_from, range_to) for _ in range(column))


def read_csv_file(file_name) -> List:
    with open(file_name, 'r') as r_file:
        file_reader = csv.reader(r_file)
        li = []
        for line in file_reader:
            li.append(line)
        return li


def generate_csv_from_input_list(file_name: str, content: List[list]):
    with open(file_name, 'w') as w_file:
        file_writer = csv.writer(w_file)

        for line in content:
            file_writer.writerow(line)


def x_out_csv_column(column: int, file_name: str):
    matrix = read_csv_file(file_name)

    for row in range(len(matrix)):
        matrix[row][column] = 'XXXXXX'

    generate_csv_from_input_list(file_name, matrix)


def o_out_csv_row(row: int, file_name: str):
    matrix = read_csv_file(file_name)

    for column in range(len(matrix[row])):
        matrix[row][column] = 'OOOOO'
    generate_csv_from_input_list(file_name, matrix)


def t_out_zigzag(file_name):
    matrix = read_csv_file(file_name)
    single_column = len(matrix[0]) - 1

    for row in range(len(matrix)):

        if row % (len(matrix[0]) - 1) == 0:

            for column in range(len(matrix[0])):
                matrix[row][column] = 'TT'

            single_column = len(matrix[0]) - 1
        else:

            single_column -= 1
            matrix[row][single_column] = 'TT'
    generate_csv_from_input_list(file_name, matrix)


def compute_average_of_a_list(li):
    li_to_int = [int(i) for i in li]
    average = sum(li_to_int) / len(li_to_int)
    li_to_int.append(average)
    li_to_str = [str(i) for i in li_to_int]
    return li_to_str


def csv_append_row_column_average(source: str, destination: str):
    matrix = read_csv_file(source)

    with open(destination, 'w') as a_file:

        file_append = csv.writer(a_file)

        for line in matrix:
            file_append.writerow(compute_average_of_a_list(line))

        column_sums = [0 for _ in range(len(matrix[0]))]

        for row in matrix:
            for ci, col_value in enumerate(row):
                column_sums[ci] += int(col_value)

        column_averages = [col_sum / len(matrix) for col_sum in column_sums]

        file_append.writerow(column_averages)


def min_max_element(source: str):
    matrix = read_csv_file(source)
    maxi = []
    mini = []
    for row in matrix:
        maxi.append(max([int(i) for i in row]))
        mini.append(min([int(i) for i in row]))
    return min(mini), max(maxi)


######################################################################################
def transpose(source: str, destination: str):
    matrix = read_csv_file(source)
    transpose_matrix = []

    with open(destination, 'w') as w_file:

        file_writer = csv.writer(w_file)

        for _ in range(len(matrix[0])):
            li = [0 for _ in range(len(matrix))]
            transpose_matrix.append(li)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transpose_matrix[col][row] = matrix[row][col]

        file_writer.writerows(transpose_matrix)


def matrix_transpose(matrix):
    m_transpose = []
    for _ in range(len(matrix[0])):
        li = [0 for _ in range(len(matrix))]
        m_transpose.append(li)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            m_transpose[col][row] = matrix[row][col]
    return m_transpose


# ################################# Second way of getting average #######################
def average_row(li):
    li_to_int = [int(i) for i in li]

    average_row = sum(li_to_int) // len(li_to_int)
    li_to_int.append(average_row)
    return li_to_int


def new_average_col_row(source: str, destination: str):
    matrix = read_csv_file(source)

    with open(destination, 'w') as w_file:

        file_writer = csv.writer(w_file)

        for row in matrix:
            file_writer.writerow(average_row(row))

        sum_columns_list = [0 for _ in range(len(matrix[0]))]

        for row in matrix:

            col_indx = 0

            for column in row:
                sum_columns_list[col_indx] += int(column)
                col_indx += 1

        average_column = [col // len(matrix) for col in sum_columns_list]
        file_writer.writerow(average_column)
###########################################################################################


def sum_multiplication_two_lists(li_one, li_two):

    return sum([li_one[i] * li_two[i] for i in range(len(li_one))])


def matrix_transpose_multiplication(source_one: str, source_two: str, destination: str):
    matrix_one = read_csv_file(source_one)
    matrix_two = read_csv_file(source_two)

    matrix_one_int = [[int(i) for i in line] for line in matrix_one]
    matrix_two_int = [[int(i) for i in line] for line in matrix_two]

    matrix_two_int_transpose = matrix_transpose(matrix_two_int)

    matrix_multi = [[0 for _ in range(len(matrix_two_int[0]))] for _ in range(len(matrix_one_int))]

    row_index = 0
    for row in matrix_one_int:
        col_index = 0
        for col in matrix_two_int_transpose:
            matrix_multi[row_index][col_index] = sum_multiplication_two_lists(row, col)
            col_index += 1
        row_index += 1

    generate_csv_from_input_list(destination, matrix_multi)
###########################################################################################


def number_of_occurrences_in_a_list(li):

    num_occ = dict()
    value = 1
    num_occ_li = []

    for i in range(len(li)):
        if li[i] in num_occ:
            num_occ[li[i]] += 1
        else:
            num_occ[li[i]] = value
    return num_occ

    # for key, val in num_occ.items():
    #     num_occ_li.append(val)
    # return num_occ_li


def num_of_occurrences_in_matrix(source: str):
    matrix = read_csv_file(source)
    num_occur_dict = {}

    for row in matrix:
        for col in row:

            if col in num_occur_dict:
                num_occur_dict[col] += 1
            else:
                num_occur_dict[col] = 1

    for row_i, row in enumerate(matrix):
        for col_i, col in enumerate(row):
            matrix[row_i][col_i] = num_occur_dict[col]
    return matrix

    # other way to update the matrix with number of occurrence
    # for row_i in range(len(matrix)):
    #     for col_i in range(len(matrix[0])):
    #         matrix_cell_value = matrix[row_i][col_i]
    #         matrix[row_i][col_i] = num_occur_dict[matrix_cell_value]


###########################################################################################
def sort_elements_in_columns(source: str):
    matrix = read_csv_file(source)
    matrix_int = [[int(i) for i in line] for line in matrix]

    matrix_int_t = matrix_transpose(matrix_int)
    sorted_matrix_transpose = []

    for line in matrix_int_t:
        sorted_lines = sorted(line)
        sorted_matrix_transpose.append(sorted_lines)

    matrix_int_t = matrix_transpose(sorted_matrix_transpose)
    return matrix_int_t


########################################### TEST ################################################
class TestTransposeMatrix(unittest.TestCase):

    def test_transpose_matrix_from_files(self):
        source = 'new_csv_file.csv'
        destin = 'transpose.csv'

        # function under test
        transpose(source, destin)

        with open(destin, "r") as actual_file:
            file_reader = csv.reader(actual_file)

            actual = [[int(val) for val in line] for line in file_reader]
            expected = [[5, 1, 2], [5, 2, 3]]

            self.assertEqual(expected, actual)

    def test_matrix_transpose(self):

        matrix = [[1, 1, 1], [2, 3, 4]]
        actual = matrix_transpose(matrix)
        expected = [[1, 2], [1, 3], [1, 4]]

        self.assertEqual(expected, actual)

    def test_sum_multiplication_two_lists(self):

        li_one = [2, 3, 1]
        li_two = [1, 2, 1]
        actual = sum_multiplication_two_lists(li_one, li_two)

        expected = 9

        self.assertEqual(expected, actual)

    def test_matrix_transpose_multiplication(self):
        source_one = 'matrix_one_x.csv'
        source_two = 'matrix_two_y.csv'
        destin = 'transpose_multiplication.csv'

        matrix_transpose_multiplication(source_one, source_two, destin)

        with open(destin, 'r') as actual_file:
            file_reader = csv.reader(actual_file)

            actual = [[int(val) for val in line] for line in file_reader]
            expected = [[2, 0], [1, 0]]

            self.assertEqual(expected, actual)


######################################################################################################
if __name__ == '__main__':
    sort_col = sort_elements_in_columns('sort_col_matrix.csv')
    print(sort_col)

    # unittest.main()
    # generate_numbers_in_csv_file('matrix_one_x.csv', 2, 3, 0, 1)


