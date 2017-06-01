from src.axiscare.cache import update_cache, get_cache


def carer_string():
    #
    try:
        #
        carers_cache = get_cache()
        #
        carer = carerFind(carers_cache['carers'])
        #
        s = 'Your {when} carer is {name}'.format(when=carer.when(),
                                                 name=carer.name())
        #
        return s
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception


def carerFind(carerDetails):
    for dt, carer in carerDetails:
        if carer.is_current() or carer.is_next():
            return carer


update_cache()
print(carer_string())