import requests
import csv


def generic_open_data_nyc_pagination_request(number, url):

    limit = min(200, number)
    offset_range = number // limit

    all_records = []

    for i in range(offset_range):

        offset = limit * i
        url_result = url + '?$' + f'limit={limit}' + '&$' + f'offset={offset}'

        response = requests.get(url_result)
        records = response.json()

        if len(records) == 0:
            return all_records
        all_records.extend(records)

    if len(all_records) < number:

        limit = number - len(all_records)
        url_result = url + '?$' + f'limit={limit}' + '&$' + f'offset={len(all_records)}'
        response = requests.get(url_result)
        records = response.json()
        all_records.extend(records)

    return all_records


def csv_includes_average_of_some_of_generic_open_data(list_all_records):

    col1 = 'total_students'
    col2 = 'students_in_temporary_housing'
    col3 = 'students_residing_in_shelter'
    col4 = 'residing_in_dhs_shelter'
    col5 = 'residing_in_non_dhs_shelter'

    li = []

    for obj in list_all_records:

        my_dict = {col1: obj[col1], col2: obj[col2], col3: obj[col3], col4: obj[col4], col5: obj[col5]}

        li.append(my_dict)

    average_dict = {col1: 0, col2: 0, col3: 0, col4: 0, col5: 0}
    for dic in li:
        for key, val in dic.items():
            if val == 's':
                average_dict[key] += 0
            else:
                average_dict[key] += int(val) / len(li)
    li.append(average_dict)

    with open('generic_open_data_nyc_pagination_request.csv', 'w') as w_file:
        fieldnames = [col4, col5, col2, col3, col1]

        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()

        for line in li:

            file_writer.writerow(line)


if __name__ == '__main__':

    urll = 'https://data.cityofnewyork.us/resource/ec4f-sy8r.json'
    result_list_all = generic_open_data_nyc_pagination_request(150, urll)

    csv_includes_average_of_some_of_generic_open_data(result_list_all)



