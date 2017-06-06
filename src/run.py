import os
from bottle import error, HTTPError
from bottle import get
from bottle import run, static_file, HTTPResponse

from src.config import cfg

from src.web.web_create_error import create_error
from src.web.web_create_home import create_home

from src.axiscare.carer_info import carer_info, carers_today
from src.weather.weather import obj_weather


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
def carers_nownext():
    data = carer_info()
    if data:
        return HTTPResponse(data, status=200)
    else:
        return HTTPResponse(status=400)

@get('/info/today')
def info_today():
    #
    data = {}
    try:
        data['carers'] = carers_today()
    except Exception as e:
        print('ERROR: Failed to add carer data to response - {error}'.format(error=e))
        data['carers'] = {}
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

run(host='localhost', port=cfg.self_port, debug=True)