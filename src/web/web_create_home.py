from urllib import urlopen
from src.config import cfg


def create_home():
    args = {'messages': ''}
    #
    return urlopen('html/header.html').read().encode('utf-8').format(title=cfg.title) + \
           urlopen('html/index.html').read().encode('utf-8').format(**args) +\
           urlopen('html/footer.html').read().encode('utf-8')