import requests as requests


def getData(url):
    #
    r = requests.get(url)
    #
    if r.status_code == requests.codes.ok:
        return r.content
    else:
        raise Exception
