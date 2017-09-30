import json
import os
import ast
from datetime import datetime


def get_json():
    with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as data_file:
        data = json.load(data_file)
    return data


def put_json(new_data):
    try:
        #
        try:
            new_data = ast.literal_eval(new_data)
        except:
            new_data = new_data
        #
        with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'w+') as output_file:
            output_file.write(json.dumps(new_data, indent=4, separators=(',', ': ')))
            output_file.close()
        #
        return True
    except Exception as e:
        return False

################################################################################################


def get_cfg_json():
    data = get_json()
    return data['config']

################################################################################################
# General
################################################################################################


def get_config_general():
    data = get_cfg_json()
    return data['general']


def get_config_general_title():
    data = get_config_general()
    return data['title']

################################################################################################
# Weather
################################################################################################


def get_config_weather():
    data = get_cfg_json()
    return data['weather']


def get_config_weather_metoffice_appkey():
    data = get_config_weather()
    return data['metoffice_appkey']


def get_config_weather_town():
    data = get_config_weather()
    return data['cfg_town']

################################################################################################
# Google
################################################################################################


def get_config_google():
    data = get_cfg_json()
    return data['google']


def get_config_google_googlesheet():
    data = get_config_google()
    return data['google_sheet']


def get_config_google_googlesheetId():
    data = get_config_google_googlesheet()
    return data['google_sheetId']


def get_config_google_googlesheetRange():
    data = get_config_google_googlesheet()
    return data['google_sheetRange']

################################################################################################
# Axiscare
################################################################################################


def get_config_axiscare():
    data = get_cfg_json()
    return data['axiscare']


def get_config_axiscare_url():
    data = get_config_axiscare()
    return data['url']


def get_config_axiscare_date():
    data = get_config_axiscare()
    return data['dateReceived']


def put_config_axiscare_url(url):
    data = get_config_axiscare()
    data['config']['axiscare']['dateReceived'] = datetime.now().strftime('%Y-%m-%d')
    data['config']['axiscare']['url'] = url
    put_json(data)

################################################################################################
# Axiscare
################################################################################################


def get_config_emailsafelist():
    data = get_cfg_json()
    return data['email_safelist']
