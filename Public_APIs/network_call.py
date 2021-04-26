import requests
from pprint import pprint
import csv


def student_health_survey__api():
    url = 'https://data.cityofnewyork.us/resource/3qty-g4aq.json'

    col1 = 'year'
    col2 = 'smoked_30days'
    col3 = 'adolescent_obesity'
    col4 = 'got_help_from_a_counselor_in_past_12_months'

    response = requests.get(url)
    my_json = response.json()

    li = []
    average_dict = {col1: 0, col2: 0, col3: 0, col4: 0}
    cols = [col1, col2, col3, col4]

    for obj in my_json:
        my_dic = {}

        for col in cols:
            average_dict[col] += float(obj[col]) if obj[col] != 'n/a' else 0
            my_dic[col] = obj[col]

        li.append(my_dic)
    average_dict = {key: val/len(li) for key, val in average_dict.items()}
    li.append(average_dict)

    with open('api.csv', 'w') as w_file:

        fieldnames = [col4, col3, col2, col1]

        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()

        for line in li:

            file_writer.writerow(line)


if __name__ == '__main__':

    student_health_survey__api()



