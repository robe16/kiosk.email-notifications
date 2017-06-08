import json
import os
import ast
from datetime import datetime


def write_json(new_data):
    try:
        #
        try:
            new_data = ast.literal_eval(new_data)
        except:
            new_data = new_data
        #
        with open(os.path.join(os.path.dirname(__file__), 'axiscare_urls.json'), 'w+') as output_file:
            output_file.write(json.dumps(new_data, indent=4, separators=(',', ': ')))
            output_file.close()
        #
        return True
    except Exception as e:
        return False


def read_json():
    with open(os.path.join(os.path.dirname(__file__), 'axiscare_urls.json'), 'r') as data_file:
        return json.load(data_file)


def get_url():
    data = read_json()
    #
    new_num = len(data['urls'])-1
    item = data['urls'][str(new_num)]
    return item['url']


def check_url(url):
    data = read_json()
    #
    for u in data['urls']:
        if data['urls'][u]['url'] == url:
            return True
    return False


def put_url(url):
    data = read_json()
    #
    new_num = len(data['urls'])
    #
    data['urls'][new_num] = {}
    data['urls'][new_num]['dateReceived'] = datetime.now().strftime('%Y-%m-%d')
    data['urls'][new_num]['url'] = url
    #
    write_json(data)