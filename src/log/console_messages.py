from datetime import datetime

timeformat = '%d/%m/%Y %H:%M:%S.%f'


def print_error(error_msg):
    _print('ERROR: {error}'.format(error = error_msg))


def print_msg(msg):
    _print('{msg}'.format(msg=msg))


def _print(msg):
    # TODO - code to add msg to log file
    print('{timestamp} - {msg}'.format(timestamp=datetime.now().strftime(timeformat),
                                       msg=msg))