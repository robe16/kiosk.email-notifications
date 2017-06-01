from src.axiscare.data import getData
from src.axiscare.parse import getCarerDetails
from src.axiscare.url import get_url

import src.cache as cache


def update_cache():
    #
    try:
        #
        url = get_url()
        #
        data = getData(url)
        #
        cache.carers = getCarerDetails(data)
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception