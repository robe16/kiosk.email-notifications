from axiscare.data import getData
from axiscare.parse import getCarerDetails
from config.cfg import get_config_axiscare_url

import cache


def update_cache():
    #
    try:
        #
        url = get_config_axiscare_url()
        #
        data = getData(url)
        #
        cache.carers = getCarerDetails(data)
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception