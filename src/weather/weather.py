from src.config.cfg import cfg_town
from data_metoffice import createForecast
from data_sunrise_sunset_org import createSunriseSet
import json
from datetime import datetime


class obj_weather():

    def __init__ (self):
        #
        self.data_cache = {}
        self.data_lastupdate = None
        #
        self.updateData()

    def weather_today(self):
        if not self.data_lastupdate.date() == datetime.now().date():
            self.updateData()
        #
        return self.data_cache

    def updateData(self):
        try:
            self.data_cache = self.getForecast()
            self.data_lastupdate = datetime.now()
        except Exception as e:
            print('ERROR: Failed to return requested weather data - {error}'.format(error=e))
            return False

    def getForecast(self):
        #
        forecast = createForecast(cfg_town)
        #
        lat = forecast['location']['latitude']
        lng = forecast['location']['longitude']
        #
        day = 0
        while day < len(forecast['days']):
            #
            forecast['days'][day]['sunRiseSet'] = createSunriseSet(forecast['days'][day]['date'],
                                                                   lat,
                                                                   lng)
            #
            day += 1
            #
        #
        return forecast
