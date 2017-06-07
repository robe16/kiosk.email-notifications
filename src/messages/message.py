from datetime import datetime


class messageDetails():

    def __init__(self, msg, start, end, countdown_target=False):
        #
        self._msg = msg
        self._start = start
        self._end = end
        self._countdown_target = countdown_target

    def msg(self):
        if self.is_current():
            if self._countdown_target:
                return self._msg.format(countdown=self.countdown_days())
            else:
                return self._msg
        else:
            return False

    def start_date(self):
        return self._start

    def end_date(self):
        return self._end

    def start_string_date(self):
        return self._start.strftime('%d/%m/%Y')

    def end_string_date(self):
        return self._end.strftime('%d/%m/%Y')

    def is_current(self):
        return self._start.date() <= datetime.now().date() <= self._end.date()

    def countdown_days(self):
        delta = self._countdown_target - datetime.now()
        return delta.days
