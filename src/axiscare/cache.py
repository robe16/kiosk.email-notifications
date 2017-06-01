from src.axiscare.data import getData
from src.axiscare.parse import getCarerDetails
from src.axiscare.url import get_url

import ast
import os
import json


def update_cache():
    #
    try:
        #
        url = get_url()
        #
        data = getData(url)
        #
        carers_all = getCarerDetails(data)
        #
        write_json(carers_all)
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception


def write_json(new_data):
    try:
        #
        try:
            new_data = ast.literal_eval(new_data)
        except:
            new_data = new_data
        #
        with open(os.path.join(os.path.dirname(__file__), 'axiscare_cache.json'), 'w+') as output_file:
            output_file.write(json.dumps(new_data, indent=4, separators=(',', ': ')))
            output_file.close()
        #
        return True
    except Exception as e:
        return False


def get_cache():
    with open(os.path.join(os.path.dirname(__file__), 'axiscare_cache.json'), 'r') as data_file:
        return json.load(data_file)