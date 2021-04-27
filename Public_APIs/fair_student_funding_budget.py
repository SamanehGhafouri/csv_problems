import requests
from pprint import pprint


def fair_student_funding_budget(number, url):

    limit = 100
    offset_range = number // limit

    all_records = []

    for i in range(offset_range):

        offset = limit * i
        url_result = url + '?$' + f'limit={limit}' + '&$' + f'offset={offset}'

        response = requests.get(url_result)
        my_json = response.json()

        if len(my_json) == 0:
            break

        all_records.extend(my_json)
    return all_records


url = 'https://data.cityofnewyork.us/resource/nbgq-j9jt.json'
result = fair_student_funding_budget(2000, url)
pprint(result)