import requests
from pprint import pprint


def get_number_of_records(number, url):

    limit = 1000
    offset_range = number // limit

    all_records = []

    for i in range(offset_range):
        offset = limit * i
        url_u = url + '?' + '$' + f'limit={limit}' + '&' + '$' + f'offset={offset}'

        response = requests.get(url_u)
        my_json = response.json()

        if len(my_json) == 0:
            break

        all_records.extend(my_json)

    return all_records


url = 'https://data.cityofnewyork.us/resource/jufi-gzgp.json'
result = get_number_of_records(2847889, url)
pprint(result)
