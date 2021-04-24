import csv
import random
from typing import List
import pprint


# create a csv file includes 4 rows and 50 columns of random float numbers
def csv_file(file_name: str, rows, columns):
    with open(file_name, 'w') as file_test:
        csv_writer = csv.writer(file_test)

        for i in range(rows):
            csv_writer.writerow([random.random() for _ in range(columns)])


#
# csv_file('abc.csv', 20, 20)
# csv_file('efg.csv', 5, 5)
# csv_file('xyz.csv', 1, 1)


# create csv file from 2D array
def new_csv(file_name: str, content: List[list]):
    with open(file_name, 'w') as file:
        csv_writer = csv.writer(file)

        for line in content:
            csv_writer.writerow(line)


matrix_s = [
    ['A', 'B', 'C'],
    [1, 2, 3],
    ['XY', 'AW', 'AZ']
]
new_csv('samaneh.csv', matrix_s)


# Read csv file
def read_csv_file(file_name: str) -> List[list]:
    with open(file_name, 'r') as file:
        csv_read = csv.reader(file)
        li = []
        for line in csv_read:
            li.append(line)

        return li


# x out row function
def x_out_row(file_name: str, row_num: int):
    matrix = read_csv_file(file_name)

    # change matrix here
    for column_index in range(len(matrix[row_num])):
        matrix[row_num][column_index] = 'xxxxx'

    new_csv(file_name, matrix)


# x out column function
def x_out_column(file_name: str, column_num: int):
    matrix = read_csv_file(file_name)

    for row in range(len(matrix)):
        matrix[row][column_num] = 'XXXXXX'

    new_csv(file_name, matrix)


# zig zag X pattern
def x_out_csv_zig_zag(file_name: str):
    matrix = read_csv_file(file_name)

    for row in range(len(matrix)):
        if row % (len(matrix[0]) - 1) == 0:
            for column in range(len(matrix[0])):
                matrix[row][column] = 'XXXXXXXXXX'
        else:
            column = (len(matrix[0]) - 1) - (row % (len(matrix[0]) - 1))
            matrix[row][column] = 'XXXXXXXXXXX'
    new_csv(file_name, matrix)


def x_out_csv_zig_zag_stefan(file_name: str):
    matrix = read_csv_file(file_name)
    single_column = len(matrix[0]) - 1

    for row in range(len(matrix)):
        if row % (len(matrix[0]) - 1) == 0:
            for column in range(len(matrix[0])):
                matrix[row][column] = 'XXXXXXXXXX'
            single_column = len(matrix[0]) - 1
        else:
            single_column -= 1
            matrix[row][single_column] = 'XXXXXXXXXXX'
    new_csv(file_name, matrix)


if __name__ == '__main__':
    # x_out_row('abc.csv', 1)

    csv_file('abc.csv', 10, 5)

    # x_out_column('abc.csv', 1)

    x_out_csv_zig_zag_stefan('abc.csv')
