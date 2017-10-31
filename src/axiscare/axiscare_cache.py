from axiscare.data import getData
from axiscare.parse import getCarerDetails
from config.cfg import get_config_axiscare_url
from log.log import log_error
import cache


def update_cache():
    #
    try:
        #
        url = get_config_axiscare_url()
        #
        if not url == '':
            data = getData(url)
            #
            cache.carers = getCarerDetails(data)
            #
        else:
            cache.carers = {}
        #
    except Exception as e:
        log_error('Error when updating Axiscare cache data - {error}'.format(error=e))
        raise Exception