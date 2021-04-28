import requests
import csv


def generate_open_data(number_of_records, url):

    limit = min(50, number_of_records)
    offset_range = number_of_records // limit
    all_records = []

    for i in range(offset_range):

        offset = limit * i
        url_api = url + '?$' + f'limit={limit}' + '&$' + f'offset={offset}'
        response = requests.get(url_api)
        records = response.json()

        if len(records) == 0:
            return all_records
        all_records.extend(records)

    if len(all_records) < number_of_records:

        limit = number_of_records - len(all_records)
        url_api = url + '?$' + f'limit={limit}' + '&$' + f'offset={len(all_records)}'
        response = requests.get(url_api)
        records = response.json()
        all_records.extend(records)

    return all_records


def csv_average(list_all_records):

    col1 = 'number_of_test_takers'
    col2 = 'critical_reading_mean'
    col3 = 'mathematics_mean'
    col4 = 'writing_mean'

    list_cols = [col1, col2, col3, col4]

    li = []
    for obj in list_all_records:
        for col in list_cols:

            if col not in obj:
                obj[col] = 0
    for obj in list_all_records:
        col_dictionary = {col1: obj[col1], col2: obj[col2], col3: obj[col3], col4: obj[col4]}
        li.append(col_dictionary)

    average_all_records_in_dict = {col1: 0, col2: 0, col3: 0, col4: 0}
    for dic in li:
        for key, val in dic.items():

            average_all_records_in_dict[key] += int(val) / len(li)

    li.append(average_all_records_in_dict)

    with open('generate_open_data_SAT', 'w') as w_file:

        fieldnames = [col2, col3, col1, col4]
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')

        file_writer.writeheader()

        for line in li:
            file_writer.writerow(line)


if __name__ == '__main__':

    record = generate_open_data(600, 'https://data.cityofnewyork.us/resource/zt9s-n5aj.json')
    csv_average(record)
