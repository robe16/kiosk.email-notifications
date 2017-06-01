from urllib import urlopen
from src.config import cfg
from src.axiscare.cache import carerString


def create_home():
    args = {'carer_msg': carerString()}
    #
    body = urlopen('html/index.html').read().encode('utf-8').format(**args)
    #
    return urlopen('html/header.html').read().encode('utf-8').format(title=cfg.title) + \
           urlopen('html/body.html').read().encode('utf-8').format(header='', body=body) +\
           urlopen('html/footer.html').read().encode('utf-8')