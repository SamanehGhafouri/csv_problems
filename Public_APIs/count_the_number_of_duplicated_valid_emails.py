import csv


def count_duplicated_valid_emails(source):

    with open(source, 'r') as r_file:

        file_reader = csv.reader(r_file)
        next(file_reader)
        matrix_data = []
        for line in file_reader:
            matrix_data.append(line)

    set_of_valid_emails = set()

    for valid_email in matrix_data:
        if valid_email[1] == 'Valid':
            set_of_valid_emails.add(valid_email[0])
    number_of_duplicated_valid_emails = len(matrix_data) - len(set_of_valid_emails)
    return number_of_duplicated_valid_emails


if __name__ == '__main__':

    number_of_duplicated = count_duplicated_valid_emails('generate_open_data_valid_invalid_email_desti.csv')
    print(number_of_duplicated)

