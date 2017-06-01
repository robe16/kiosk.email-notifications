from src.axiscare.data import getData
from src.axiscare.parse import getCarerNext
from src.axiscare.url import get_url


def carerString():
    #
    try:
        #
        url = get_url()
        #
        data = getData(url)
        #
        carerDetails = getCarerNext(data)
        #
        # {'when': 'now', 'name': c['name'], 'start': c['start'], 'end': c['end']}
        #
        s = 'Your {when} carer is {name}'.format(when=carerDetails['when'],
                                                 name=carerDetails['name'])
        #
        return s
        #
    except Exception as e:
        print('ERROR: {error}'.format(error=e))
        raise Exception