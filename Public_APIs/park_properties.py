import requests
import csv


def park_properties():

    url = 'https://data.cityofnewyork.us/resource/enfh-gkve.json'

    col1 = 'objectid'
    col2 = 'us_congress'
    col3 = 'zipcode'
    col4 = 'nys_senate'
    col5 = 'nys_assembly'

    response = requests.get(url)
    my_json = response.json()
    li = []

    for data in my_json:

        my_dic = {col1: data[col1], col2: data[col2],  col3: data[col3], col4: data[col4], col5: data[col5]}
        li.append(my_dic)

    average_col = {col1: 0, col2: 0, col3: 0, col4: 0, col5: 0}
    for dc in li:
        for key, val in dc.items():
            average_col[key] += int(val) / len(li)
    li.append(average_col)

    with open('park_properties.csv', 'w') as w_file:
        fieldnames = [col5, col4, col1, col2, col3]
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')

        file_writer.writeheader()

        for line in li:

            file_writer.writerow(line)


if __name__ == '__main__':
    park_properties()

