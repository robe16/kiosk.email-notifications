from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from axiscare.carer import carerVisit


def getCarerDetails(data):
    #
    soup = BeautifulSoup(data, "html.parser")
    #
    carers_all = {}
    #
    for x in range(0,2):
        dt = datetime.now() + timedelta(days=x)
        carers = parseDailyCarers(soup, dt)
        carers_all.update(carers)
    #
    return carers_all


def parseDailyCarers(soup, d):
    #
    carers = {}
    #
    class_filter = "calendar-day-{date}".format(date=d.strftime("%Y-%m-%d"))
    dayitem = soup.findAll("td", {"class": class_filter})[0]
    #
    daydetails = dayitem.findAll("td", {"class": "calendar_event_cell"})[0]
    careritems = daydetails.findAll("table", {"class": "cal_item cal_item_visit visit_assigned"})
    #
    for i in careritems:
        cTime = i.findAll("span", {"class": "cal_time"})[0].string
        cTime = cTime[:-((cTime.index(')'))-(cTime.index(' (')-2))]
        #
        cStart = datetime.combine(d.date(), datetime.strptime(cTime[:5], '%H:%M').time())
        cEnd = datetime.combine(d.date(), datetime.strptime(cTime[6:], '%H:%M').time())
        #
        cName = i.findAll("tr", {"class": "person caregiver assigned"})[0].contents[0].string
        #
        c = carerVisit(cName, cStart, cEnd)
        #
        carers[c.start_string_datetime()] = c
        #
    return carers


def checkCarers(carers, dt):
    #
    for c in carers:
        if c['start']>datetime.now():
            return {'when': 'next',
                    'name': c['name'],
                    'start': c['start'],
                    'end': c['end']}
        elif c['start']>datetime.now() and c['end']>datetime.now():
            return {'when': 'current',
                    'name': c['name'],
                    'start': c['start'],
                    'end': c['end']}
    #
    raise False