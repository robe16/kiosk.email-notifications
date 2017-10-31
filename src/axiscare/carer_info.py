from axiscare.axiscare_cache import update_cache
from log.log import log_error
import cache

def carer_info():
    #
    try:
        #
        carer = carerFind_nownext(cache.carers)
        #
        if not bool(carer):
            update_cache()
            carer = carerFind_nownext(cache.carers)
        #
        if not bool(carer):
            raise Exception('No details of carers held in cache')
        #
        carer_details = {"carer": {"label": carer.label(),
                                   "name": carer.name(),
                                   "start": carer.start_string_datetime(),
                                   "end": carer.end_string_datetime()}
                         }
        #
        return carer_details
        #
    except Exception as e:
        log_error('Error gathering and returning current/next carer details - {error}'.format(error=e))
        raise Exception


def carerFind_nownext(carers_all):
    for key in sorted(carers_all.keys()):
        carer = carers_all[key]
        if carer.is_current() or carer.is_future():
            return carer
    return False


def carers_today():
    #
    try:
        #
        c_list = carerFind_today(cache.carers)
        #
        if len(c_list) == 0:
            update_cache()
            carer = carerFind_today(cache.carers)
        #
        return c_list
        #
    except Exception as e:
        log_error('Error getting today\'s carers - {error}'.format(error=e))
        raise Exception


def carerFind_today(carers_all):
    c_list = []
    for key in sorted(carers_all.keys()):
        carer = carers_all[key]
        if carer.is_today():
            c = {"name": carer.name(),
                 "start": carer.start_string_datetime(),
                 "end": carer.end_string_datetime()}
            c_list.append(c)
    #
    return c_list
