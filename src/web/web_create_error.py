from urllib import urlopen


def create_error(code):
    if code == 404:
        args = {'code': '404',
                'desc': 'Page not found',
                'mesg': 'The page you are looking for does not exist!!'}
    elif code == 500:
        args = {'code': '500',
                'desc': 'Network error',
                'mesg': 'There was an error with the code on the server!!'}
    else:
        args = {'code': '---',
                'desc': 'Unknown',
                'mesg': 'An error has been encountered, please try again!!'}
    #
    body = urlopen('html/error.html').read().encode('utf-8').format(**args)
    #
    return urlopen('html/header.html').read().encode('utf-8').format(title=str(code)) + \
           urlopen('html/body.html').read().encode('utf-8').format(header='', body=body) +\
           urlopen('html/footer.html').read().encode('utf-8')