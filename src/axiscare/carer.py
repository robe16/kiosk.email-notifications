from datetime import datetime


class carerVisit():

    def __init__(self, name, start, end):
        #
        self._name = name
        self._start = start
        self._end = end

    def name(self):
        return self._name

    def start_datetime(self):
        return self._start

    def end_datetime(self):
        return self._end

    def start_string_time(self):
        return self._start.strftime('%H:%M')

    def end_string_time(self):
        return self._end.strftime('%H:%M')

    def start_string_datetime(self):
        return self._start.strftime('%Y-%m-%d %H:%M')

    def end_string_datetime(self):
        return self._end.strftime('%Y-%m-%d %H:%M')

    def is_current(self):
        return self._start < datetime.now() and self._end > datetime.now()

    def is_future(self):
        return self._start > datetime.now()

    def when(self):
        if self.is_current():
            return 'current'
        elif self.is_future():
            return 'next'
        else:
            return False
