from src.axiscare.cache import update_cache
import src.cache as cache

def carer_string():
    #
    try:
        #
        carer = carerFind(cache.carers)
        #
        if not bool(carer):
            update_cache()
            carer = carerFind(cache.carers)
        #
        return carer.label()
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception


def carerFind(carerDetails):
    for key in sorted(carerDetails.keys()):
        carer = carerDetails[key]
        if carer.is_current() or carer.is_future():
            return carer
    return False