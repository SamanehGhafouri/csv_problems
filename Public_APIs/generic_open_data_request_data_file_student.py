import requests
import csv


def generic_open_data_request_data_file_student(number, url):

    limit = min(100, number)
    offset_range = limit // number
    all_records = []

    for i in range(offset_range):

        offset = limit * i
        url_request = url + '?$' + f'limit={limit}' + '&$' + f'offset={offset}'
        response = requests.get(url_request)
        records = response.json()

        if len(records) == 0:
            return all_records
        all_records.extend(records)

    if len(all_records) < number:

        limit = number - len(all_records)
        url_request = url + '?$' + f'limit={limit}' + '&$' + f'offset={len(all_records)}'
        response = requests.get(url_request)
        records = response.json()
        all_records.extend(records)

    return all_records


def csv_average(list_all_records):

    col1 = 'total_parent_response_rate'
    col2 = 'total_teacher_response_rate'
    col3 = 'total_student_response_rate'

    li = []

    for obj in list_all_records:

        dictionary_cols = {col1: obj[col1], col2: obj[col2], col3: obj[col3]}
        li.append(dictionary_cols)

    average_dictionary = {col1: 0, col2: 0, col3: 0}
    for dict in li:
        for key, val in dict.items():
            average_dictionary[key] += float(val) / len(li)
    li.append(average_dictionary)

    with open('generic_open_data_request_data_file_student.csv', 'w') as w_file:

        fieldnames = [col1, col2, col3]
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()

        for line in li:
            file_writer.writerow(line)


if __name__ == '__main__':

    rec_all = generic_open_data_request_data_file_student(30000, 'https://data.cityofnewyork.us/resource/fb6n-h22r.json')
    csv_average(rec_all)
