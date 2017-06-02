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
        return self._start.strftime('%Y-%m-%dT%H:%M')

    def end_string_datetime(self):
        return self._end.strftime('%Y-%m-%dT%H:%M')

    def is_today(self):
        return self._start.date() == datetime.now().date()

    def is_current(self):
        return self._start < datetime.now() and self._end > datetime.now()

    def is_future(self):
        return self._start > datetime.now()

    def label(self):
        return '{when} is {name}'.format(when=self.when(),
                                         name=self._name)

    def when(self):
        if self.is_current():
            return 'Your current carer'
        elif self.is_future():
            #
            if self._start.time() < datetime.strptime('12:00', '%H:%M').time():
                morning_afternoon = 'morning'
            else:
                morning_afternoon = 'afternoon'
            #
            if self._start.date() > datetime.now().date():
                return 'Your carer tomorrow {morning_afternoon}'.format(morning_afternoon=morning_afternoon)
            else:
                return 'Your carer this {morning_afternoon}'.format(morning_afternoon=morning_afternoon)
            #
        else:
            raise Exception
