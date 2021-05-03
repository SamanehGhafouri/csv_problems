import re
import csv
import requests


def data_from_api(number, get_url):
    limit = min(200000, number)
    offset_range = limit // number

    all_records = []
    for i in range(offset_range):
        offset = limit * i
        url_all = get_url + '?$' + f'limit={limit}' + '&$' + f'offset={offset}'
        response = requests.get(url_all)
        records = response.json()
        if len(records) == 0:
            return all_records
        all_records.extend(records)

    if len(all_records) < number:
        limit = number - len(all_records)
        url_all = get_url + '?$' + f'limit={limit}' + '&$' + f'offset={len(all_records)}'
        response = requests.get(url_all)
        records = response.json()
        all_records.extend(records)
    return all_records


def get_emails_from_all_records(li):

    col1 = 'email'

    email_list = []
    for obj in li:
        if col1 in obj:
            email_dict = {col1: obj[col1]}
            email_list.append(email_dict)
    return email_list


def write_emails_file(li, destination):
    col1 = 'email'
    with open(destination, 'w') as w_file:
        fieldnames = [col1]
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()

        for line in li:
            file_writer.writerow(line)


def reading_email_csv(source):

    with open(source, 'r') as r_file:

        matrix_data = []
        file_reader = csv.reader(r_file)
        next(file_reader)
        for line in file_reader:
            if is_email_valid(line[-1]) == 'Valid':
                line.append('Valid')
                matrix_data.append(line)
            else:
                line.append('InValid')
                matrix_data.append(line)
        return matrix_data


def count_how_many_invalid_email(source):

    matrix_data = reading_email_csv(source)
    count = 0
    for line in matrix_data:
        if line[-1] == 'InValid':
            count += 1
    return count


def write_emails_valid_invalid(source, destination):

    col1 = 'Email'
    col2 = 'Valid/InValid'

    with open(destination, 'w') as w_file:
        fieldnames = [col1, col2]
        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        matrix_data = reading_email_csv(source)
        file_writer.writeheader()

        file_writer = csv.writer(w_file)
        for line in matrix_data:
            file_writer.writerow(line)


def is_email_valid(email: str):
    valid_email = re.match(r'^\D([a-zA-Z0-9\.]+)@([a-zA-Z]+)\.([a-zA-Z]+)$', email)

    if valid_email is None:
        return 'Invalid'
    else:
        before_at = valid_email.group(1)
        after_at = valid_email.group(2)
        after_dot = valid_email.group(3)

        if len(before_at) <= 50 and len(after_at) <= 50 and 2 <= len(after_dot) <= 6:
            return "Valid"
        else:
            return "Invalid"


if __name__ == '__main__':
    # em = "san9sdf@gmail.coppori"
    # result = is_email_valid(em)
    # print(result)
    url = 'https://data.cityofnewyork.us/resource/867j-5pgi.json'
    all_record = data_from_api(400000, url)
    # pprint(all_record)
    all_email_list = get_emails_from_all_records(all_record)
    # print(all_email_list)
    # write_emails_file(all_email_list, 'generate_open_data_valid_invalid_email.csv')
    email_valid_invalid_data = reading_email_csv('generate_open_data_valid_invalid_email.csv')
    # write_emails_valid_invalid('generate_open_data_valid_invalid_email.csv', 'generate_open_data_valid_invalid_email_desti.csv')
    number_of_invalid = count_how_many_invalid_email('generate_open_data_valid_invalid_email.csv')
    print(number_of_invalid)