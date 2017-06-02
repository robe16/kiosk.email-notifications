from src.axiscare.cache import update_cache
import src.cache as cache

def carer_info():
    #
    try:
        #
        carer = carerFind(cache.carers)
        #
        if not bool(carer):
            update_cache()
            carer = carerFind(cache.carers)
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
        print('ERROR: {error}'.format(error=e))
        raise Exception


def carerFind(carers_all):
    for key in sorted(carers_all.keys()):
        carer = carers_all[key]
        if carer.is_current() or carer.is_future():
            return carer
    return False