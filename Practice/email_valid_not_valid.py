import re
import csv


def is_email_valid(email: str):
    valid_email = re.match(r'^([a-zA-Z0-9\.]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)$', email)

    if valid_email is None:
        return 'Invalid'
    else:
        before_at = valid_email.group(1)
        after_at = valid_email.group(2)
        after_dot = valid_email.group(3)

        if len(before_at) <= 50 and len(after_at) <= 50 and 2 <= len(after_dot) <= 3:
            return "Valid"
        else:
            return "Invalid"


def read_file(source):

    with open(source, 'r') as r_file:

        file_reader = csv.reader(r_file)
        matrix_data = []
        next(file_reader)
        for line in file_reader:
            if is_email_valid(line[-1]) == 'Valid':
                line.append('Valid')
                matrix_data.append(line)
            else:
                line.append('InValid')
                matrix_data.append(line)
        return matrix_data


def write_to_file(source, destination):

    with open(destination, 'w') as w_file:
        fieldnames = ['Student_Name', 'Email', 'Valid/InValid Email']

        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        matrix_data = read_file(source)
        file_writer.writeheader()

        file_writer = csv.writer(w_file)
        for line in matrix_data:
            file_writer.writerow(line)


if __name__ == '__main__':

    em = "@gmail.com"
    result = is_email_valid(em)
    print(result)
    result = read_file('valid_invalid_emails.csv')
    print(result)
    write_to_file('valid_invalid_emails.csv', 'show_valid_invalid_emails.csv')


