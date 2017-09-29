import os
import sys
from bottle import error, HTTPError, get, run, static_file, HTTPResponse

from config import cfg

from web.web_create_error import create_error
from web.web_create_home import create_home

from log.console_messages import print_error

from axiscare.url_process import start_url_updater
from axiscare.carer_info import carer_info, carers_today
from weather.weather import obj_weather
from messages.message_info import messages_current


################################
# Receive sys arguments
################################
# First argument passed through is the
# port the application listens on
try:
    self_port = sys.argv[1]
except:
    self_port = 8080  # default port
#
################################################################################################
# Create required objects
################################################################################################

weather = obj_weather()

################################################################################################
# Web UI
################################################################################################

@get('/')
def web_home():
    return HTTPResponse(body=create_home(), status=200)


################################################################################################
# Resources
################################################################################################

@get('/carers/now-or-next')
def _carers_nownext():
    try:
        data = carer_info()
        if data:
            return HTTPResponse(data, status=200)
        else:
            return HTTPResponse(status=400)
    except Exception as e:
        print_error('Could not return current/next carer details to client - {error}'.format(error=e))
        raise HTTPError(500)


@get('/messages/current')
def _messages_current():
    try:
        data = messages_current()
        if data:
            return HTTPResponse(data, status=200)
        else:
            return HTTPResponse(status=400)
    except Exception as e:
        print_error('Could not return messages to client - {error}'.format(error=e))
        raise HTTPError(500)


@get('/info/today')
def _info_today():
    #
    data = {}
    #carers
    try:
        data['carers'] = carers_today()
    except Exception as e:
        print('ERROR: Failed to add carer data to response - {error}'.format(error=e))
        data['carers'] = {}
    #weather
    try:
        data['weather'] = weather.weather_today()
    except Exception as e:
        print('ERROR: Failed to add weather data to response - {error}'.format(error=e))
        data['weather'] = {}
    #
    if data:
        return HTTPResponse(data, status=200)
    else:
        return HTTPResponse(status=400)


################################################################################################
# Static files
################################################################################################

@get('/static/<folder>/<filename>')
def get_resource(folder, filename):
    return static_file(filename, root=os.path.join(os.path.dirname(__file__),('html/static/{folder}'.format(folder=folder))))

################################################################################################
# Image files
################################################################################################

# @get('/favicon.ico')
# def send_favicon():
#     root = os.path.join(os.path.dirname(__file__), '..', 'img/logo')
#     return static_file('favicon.ico', root=root)
#
#
# @get('/img/<category>/<filename>')
# def get_image(category, filename):
#     root = os.path.join(os.path.dirname(__file__), '..', 'img/{img_cat}'.format(img_cat=category))
#     mimetype = filename.split('.')[1]
#     return static_file(filename, root=root, mimetype='image/{mimetype}'.format(mimetype=mimetype))


################################################################################################
# Error pages/responses
################################################################################################

@error(404)
def error404(error):
    return HTTPResponse(body=create_error(404), status=404)


@error(500)
def error500(error):
    return HTTPResponse(body=create_error(500), status=500)


################################################################################################

start_url_updater()
run(host='localhost', port=self_port, debug=True)