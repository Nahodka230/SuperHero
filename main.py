import requests
import operator
from pprint import pprint
# def get_json(self):
#
# #     print(type(response))
#     return response
if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    name_list = [ 'Hulk', 'Captain America', 'Thanos']
    result_dict ={}
    for hero in response:
        if hero['name'] in name_list:
            result_dict[hero['name']] = hero['powerstats']['intelligence']
    sorted_list = sorted(result_dict.items(), key=operator.itemgetter(1))
    print(f'Самый умный {sorted_list[-1][0]}, его интеллект {sorted_list[-1][1]}')