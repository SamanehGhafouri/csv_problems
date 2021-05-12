import requests
import csv
import sqlite3
from pprint import pprint
import re


def records_in_url(url, limit):

    li = []

    while True:
        query = url + f'?$limit={limit}&$offset={len(li)}'
        response = requests.get(query)
        records = response.json()
        li.extend(records)

        if len(records) < limit:
            # terminate while loop because we know
            # the next query will return 0 records
            break

        # TODO: remove me after development
        break

    col1 = 'license_nbr'
    col2 = 'business_name'
    col3 = 'contact_phone'
    li_columns = [col1, col2, col3]
    li_of_needed_records = []
    for obj in li:
        for col in li_columns:
            if col not in obj:
                obj[col] = 'N/A'
    for obj in li:
        obj_dict = {col1: obj[col1], col2: obj[col2], col3: obj[col3]}
        li_of_needed_records.append(obj_dict)
    return li_of_needed_records


def write_csv(source, destination):

    with open(destination, 'w') as w_file:

        fieldnames = ['BusinessName', 'BusinessNumber', 'ContactNumber', 'FirstName', 'LastName']
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()
        for line in source:
            file_writer.writerow(line)


def extract_first_last_or_business_name(business_name):

    valid_first_last_name = re.match(r'^([a-zA-Z]+),\s([a-zA-Z\s]+)$', business_name)
    if valid_first_last_name:
        first_name = valid_first_last_name.group(1)
        last_name = valid_first_last_name.group(2)
        return {'FirstName': f'{first_name}', 'LastName': f'{last_name}'}
    return {'BusinessName': business_name}


def data_table(records_li):

    col1 = 'FirstName'
    col2 = 'LastName'
    col3 = 'BusinessName'
    col4 = 'ContactNumber'
    col5 = 'BusinessNumber'
    # li_cols = [col1, col2, col3, col4, col5]
    records_key = ['license_nbr', 'business_name', 'contact_phone']
    for obj in records_li:
        for col in records_key:
            if col not in obj:
                obj[col] = 'N/A'

    new_li_records = []
    for obj in records_li:
        first_last_business_dict = extract_first_last_or_business_name(obj[records_key[1]])
        if len(first_last_business_dict) == 2:
            new_records_dictionary = {col3: 'N/A', col4: obj[records_key[2]], col5: obj[records_key[0]]}
            new_records_dictionary.update(first_last_business_dict)
            new_li_records.append(new_records_dictionary)
        new_records_dictionary = {col1: 'N/A', col2: 'N/A', col3: obj[records_key[1]], col4: obj[records_key[2]],
                                  col5: obj[records_key[0]]}
        new_li_records.append(new_records_dictionary)
    return new_li_records


if __name__ == '__main__':
    all_records = records_in_url('https://data.cityofnewyork.us/resource/w7w3-xahh.json', 500)

    modified_records = data_table(all_records)
    pprint(modified_records)

    write_csv(modified_records, 'database_csv_taking_records.csv')




