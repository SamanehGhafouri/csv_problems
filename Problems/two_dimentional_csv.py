import csv
from typing import List


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