import requests
from pprint import pprint
import csv


def student_health_survey__api():
    url = 'https://data.cityofnewyork.us/resource/3qty-g4aq.json'

    response = requests.get(url)
    my_json = response.json()

    li = []
    for obj in my_json:
        my_dic = {
            'year': obj['year'],
            'smoked_30days': obj['smoked_30days'],
            'adolescent_obesity': obj['adolescent_obesity'],
            'got_help_from_a_counselor_in_past_12_months': obj['got_help_from_a_counselor_in_past_12_months']
        }

        li.append(my_dic)
    pprint(li)

    with open('api.csv', 'w') as w_file:

        fieldnames = ['adolescent_obesity', 'got_help_from_a_counselor_in_past_12_months', 'smoked_30days', 'year']

        file_writer = csv.DictWriter(w_file, fieldnames=fieldnames, delimiter=',')
        file_writer.writeheader()

        for line in li:

            file_writer.writerow(line)

