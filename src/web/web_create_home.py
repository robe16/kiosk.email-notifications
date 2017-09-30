from urllib import urlopen
from config.cfg import get_config_general_title


def create_home():
    args = {'messages': ''}
    #
    return urlopen('html/header.html').read().encode('utf-8').format(title=get_config_general_title()) + \
           urlopen('html/index.html').read().encode('utf-8').format(**args) +\
           urlopen('html/footer.html').read().encode('utf-8')